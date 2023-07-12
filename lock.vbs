Option Explicit
Dim TaskName,App_FullPath,strTime
Dim NIC1, Nic, StrIP
Dim intstartaddress, intendaddress, strsubnet, strcomputer
Dim ws, strtask, exitcode

intstartaddress = 1
intendaddress = 254
strsubnet = "10.0.10."

TaskName = "lockscreen"
App_FullPath = "C:\Windows\System32\rundll32.exe user32.dll, LockWorkStation"
strTime = "19:00"

For i = intstartaddress to intendaddress
    strcomputer = strsubnet & i

Set NIC1 = GetObject("winmgmts:").InstancesOf("Win32_NetworkAdapterConfiguration")

For Each Nic in NIC1

    if Nic.IPEnabled then
        StrIP = Nic.IPAddress(0)

      'if StrIP <> strcomputer Then exitcode
        
Else Call CreateTask(TaskName,App_FullPath,strTime)

Sub CreateTask(TaskName,App_FullPath,strTime)

  Set ws = CreateObject("Wscript.Shell")
  strtask = "schtasks /create /sc Daily /tn "& qq(TaskName) & _
          " /tr "& qq(App_FullPath) & _
          " /st " & strTime & " /f"

  exitcode = ws.Run(strtask, 0, True)

  If exitcode <> 0 Then
  End If
End Sub 

Function qq(str)
    qq = chr(34) & str & chr(34)
End Function