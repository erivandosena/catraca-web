#define MyAppName "Catraca"
#define MyAppVersion "Beta"
#define MyAppPublisher "UNILAB - Universidade da Integração Internacional da Lusofonia Afro-Brasileira"
#define MyAppURL "http://catraca.unilab.edu.br/"
#define MyAppExeName "Catraca.exe"

[Setup]

AppId={{5A8261FA-E5F0-4E9C-8DCD-5B6A24B0C5EE}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
LicenseFile=..\documentos\LICENSE.txt
InfoBeforeFile=..\documentos\NOTICE.txt
InfoAfterFile=..\documentos\depois.txt
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked


[Files]
Source: ".\Catraca.exe"; DestDir: "{app}"; Flags: ignoreversion


[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon


[Registry]
;Iniciar automaticamente
Root: HKLM; Subkey: "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "catraca"; ValueData: "{app}\Catraca.exe"; Flags: uninsdeletekey 


[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent