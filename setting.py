import os
import platform

# 获取当前绝对路径
tools_path = os.getcwd()

if platform.system() == 'Windows':
    java8_path = (tools_path + "\java_path\jre1.8.0_391\\bin\java").replace('\\', '\\\\')
    java9_path = (tools_path + "\java_path\java9_win\\bin\java").replace('\\', '\\\\')
    java17_path = (tools_path + "\java_path\jdk-17.0.8\\bin\java").replace('\\', '\\\\')

else:
    # MacOS和Linux的java绝对路径
    java8_path = tools_path + "/Java_path/java_1.8/bin/java"
    java9_path = tools_path + "/Java_path/java9/bin/java"
