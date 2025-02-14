package com.yausername.youtubedl_android;

import android.app.Application;
import android.support.annotation.Nullable;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.orhanobut.logger.AndroidLogAdapter;
import com.orhanobut.logger.Logger;
import com.yausername.youtubedl_android.mapper.VideoInfo;
import com.yausername.youtubedl_android.utils.StreamGobbler;
import com.yausername.youtubedl_android.utils.StreamProcessExtractor;
import com.yausername.youtubedl_android.utils.YoutubeDLUtils;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

public class YoutubeDL {

    private static final YoutubeDL INSTANCE = new YoutubeDL();
    protected static final String baseName = "youtubedl-android";
    private static final String packagesRoot = "packages";
    private static final String pythonBin = "usr/bin/python";
    protected static final String youtubeDLName = "youtube-dl";
    private static final String youtubeDLBin = "__main__.py";
    protected static final String youtubeDLFile = "youtube_dl.zip";

    private boolean initialized = false;
    private File pythonPath;
    private File youtubeDLPath;
    private File binDir;
    private String ENV_LD_LIBRARY_PATH;
    private String ENV_SSL_CERT_FILE;

    protected static final ObjectMapper objectMapper = new ObjectMapper();

    private YoutubeDL(){
    }

    public static YoutubeDL getInstance() {
        return INSTANCE;
    }

    synchronized public void init(Application application) throws YoutubeDLException {
        if (initialized) return;

        initLogger();

        File baseDir = new File(application.getFilesDir(), baseName);
        if(!baseDir.exists()) baseDir.mkdir();

        File packagesDir = new File(baseDir, packagesRoot);
        binDir = new File(packagesDir, "usr/bin");
        pythonPath = new File(packagesDir, pythonBin);

        File youtubeDLDir = new File(baseDir, youtubeDLName);
        youtubeDLPath = new File(youtubeDLDir, youtubeDLBin);

        ENV_LD_LIBRARY_PATH = packagesDir.getAbsolutePath() + "/usr/lib";
        ENV_SSL_CERT_FILE = packagesDir.getAbsolutePath() + "/usr/etc/tls/cert.pem";

        initPython(application, packagesDir);
        initYoutubeDL(application, youtubeDLDir);

        initialized = true;
    }

    protected void initYoutubeDL(Application application, File youtubeDLDir) throws YoutubeDLException {
        if (!youtubeDLDir.exists()) {
            youtubeDLDir.mkdirs();
            try {
                YoutubeDLUtils.unzip(application.getResources().openRawResource(R.raw.youtube_dl), youtubeDLDir);
            } catch (IOException e) {
                YoutubeDLUtils.delete(youtubeDLDir);
                throw new YoutubeDLException("failed to initialize", e);
            }
        }
    }

    protected void initPython(Application application, File packagesDir) throws YoutubeDLException {
        if (!pythonPath.exists()) {
            if (!packagesDir.exists()) {
                packagesDir.mkdirs();
            }
            try {
                YoutubeDLUtils.unzip(application.getResources().openRawResource(R.raw.python3_7_arm), packagesDir);
            } catch (IOException e) {
                // delete for recovery later
                YoutubeDLUtils.delete(pythonPath);
                throw new YoutubeDLException("failed to initialize", e);
            }
            pythonPath.setExecutable(true);
        }
    }

    private void initLogger() {
        Logger.addLogAdapter(new AndroidLogAdapter() {
            @Override
            public boolean isLoggable(int priority, @Nullable String tag) {
                return BuildConfig.DEBUG;
            }
        });
    }

    private void assertInit() {
        if (!initialized) throw new IllegalStateException("instance not initialized");
    }

    public VideoInfo getInfo(String url) throws YoutubeDLException {
        YoutubeDLRequest request = new YoutubeDLRequest(url);
        request.setOption("--dump-json");
        YoutubeDLResponse response = execute(request, null);

        VideoInfo videoInfo;

        try {
            videoInfo = objectMapper.readValue(response.getOut(), VideoInfo.class);
        } catch (IOException e) {
            throw new YoutubeDLException("Unable to parse video information", e);
        }

        return videoInfo;
    }

    public YoutubeDLResponse execute(YoutubeDLRequest request) throws YoutubeDLException {
        return execute(request, null);
    }

    public YoutubeDLResponse execute(YoutubeDLRequest request, @Nullable DownloadProgressCallback callback) throws YoutubeDLException {
        assertInit();

        YoutubeDLResponse youtubeDLResponse;
        Process process;
        int exitCode;
        StringBuffer outBuffer = new StringBuffer(); //stdout
        StringBuffer errBuffer = new StringBuffer(); //stderr
        long startTime = System.currentTimeMillis();

        List<String> args = request.buildCommand();
        List<String> command = new ArrayList<>();
        command.addAll(Arrays.asList(pythonPath.getAbsolutePath(), youtubeDLPath.getAbsolutePath()));
        command.addAll(args);

        ProcessBuilder processBuilder = new ProcessBuilder(command);
        Map<String, String> env = processBuilder.environment();
        env.put("LD_LIBRARY_PATH", ENV_LD_LIBRARY_PATH);
        env.put("SSL_CERT_FILE", ENV_SSL_CERT_FILE);
        env.put("PATH",  System.getenv("PATH") + ":" + binDir.getAbsolutePath());

        try {
            process = processBuilder.start();
        } catch (IOException e) {
            throw new YoutubeDLException(e);
        }

        InputStream outStream = process.getInputStream();
        InputStream errStream = process.getErrorStream();

        StreamProcessExtractor stdOutProcessor = new StreamProcessExtractor(outBuffer, outStream, callback);
        StreamGobbler stdErrProcessor = new StreamGobbler(errBuffer, errStream);

        try {
            stdOutProcessor.join();
            stdErrProcessor.join();
            exitCode = process.waitFor();
        } catch (InterruptedException e) {
            throw new YoutubeDLException(e);
        }

        String out = outBuffer.toString();
        String err = errBuffer.toString();

        if (exitCode > 0) {
            throw new YoutubeDLException(err);
        }

        long elapsedTime = System.currentTimeMillis() - startTime;

        youtubeDLResponse = new YoutubeDLResponse(command, exitCode, elapsedTime, out, err);

        return youtubeDLResponse;
    }

    synchronized public YoutubeDLUpdater.UpdateStatus updateYoutubeDL(Application application) throws YoutubeDLException {
        try {
            return YoutubeDLUpdater.update(application);
        } catch (IOException e) {
            throw new YoutubeDLException("failed to update youtube-dl", e);
        }
    }
}
