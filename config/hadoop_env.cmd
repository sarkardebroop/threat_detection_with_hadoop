@REM Set Hadoop-specific environment variables here.

@REM The java implementation to use.
@SET JAVA_HOME=C:\Program Files\Java\jdk-17

@REM Set Hadoop home directory
@SET HADOOP_HOME=C:\Users\DEBROOP\Downloads\hadoop-3.3.6

@REM Increase heap size if needed
@SET HADOOP_HEAPSIZE=512

@REM Set log directory
@SET HADOOP_LOG_DIR=%HADOOP_HOME%\logs

@REM Where log files are stored
@SET HADOOP_CONF_DIR=%HADOOP_HOME%\etc\hadoop

@REM Native libraries path
@SET HADOOP_OPTS=-Djava.library.path=%HADOOP_HOME%\lib\native

@REM Recommended for Windows systems
@SET PATH=%PATH%;%HADOOP_HOME%\bin

@REM Optional: Silence IPv6 warnings on Windows
@SET HADOOP_OPTS=%HADOOP_OPTS% -Djava.net.preferIPv4Stack=true
