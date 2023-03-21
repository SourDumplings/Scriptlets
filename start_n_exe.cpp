/*
 * @Author: SourDumplings
 * @Date: 2023-03-21 11:40:42
 * @Link: https://github.com/SourDumplings/
 * @Email: changzheng300@foxmail.com
 * @Description: 多开 windows exe 程序
 */
#include <windows.h>
#include <iostream>
#include <string>
#include <thread>
#include <chrono>
#include <tlhelp32.h>
#include <tchar.h>
#include <cassert>

using namespace std;

DWORD getProcessIdByName(LPCTSTR name)
{
    PROCESSENTRY32 pe32;
    HANDLE hSnapshot = NULL;
    DWORD pid = -1;

    pe32.dwSize = sizeof(PROCESSENTRY32);
    hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);

    if (Process32First(hSnapshot, &pe32))
    {
        do
        {
            if (_tcsicmp(pe32.szExeFile, name) == 0)
            {
                pid = pe32.th32ProcessID;
                break;
            }
        } while (Process32Next(hSnapshot, &pe32));
    }

    CloseHandle(hSnapshot);
    return pid;
}

void hideProcess(int processId)
{
    // 获取 printArgs.exe 进程句柄
    HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, processId);

    // 隐藏进程
    if (hProcess != NULL)
    {
        DWORD dwHide = 1;
        WriteProcessMemory(hProcess, &dwHide, &dwHide, sizeof(DWORD), NULL);
    }

    // 关闭句柄
    CloseHandle(hProcess);

    printf("Process %d has been hiden.", processId);
}

int startExe(const string &cmd, const string &processName, int idx, bool needHide = false)
{
    STARTUPINFO si;
    PROCESS_INFORMATION pi;
    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);

    string windowName = processName + to_string(idx);
    si.lpTitle = LPSTR(windowName.c_str());
    CreateProcess(NULL, (LPSTR)cmd.c_str(), NULL, NULL, FALSE, CREATE_NEW_CONSOLE, NULL, NULL, &si, &pi);
    int processId = getProcessIdByName((processName + ".exe").c_str());
    assert(processId != -1);

    if (needHide)
    {
        hideProcess(processId);
    }
    return processId;
}

int main()
{
    const int N = 2;
    const string PROCESSNAME = "printArgs";
    const string CMD = "./" + PROCESSNAME + ".exe param1 param2 param3";

    for (int i = 0; i < N - 1; ++i)
    {
        startExe(CMD, "printArgs", i, true);
        this_thread::sleep_for(chrono::seconds(5));
    }

    startExe(CMD, "printArgs", N - 1);
    return 0;
}
