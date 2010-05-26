#!/usr/bin/expect --

set argv [linsert $argv 0 "--define" ]
set argv [linsert $argv 1 "_signature gpg" ]
set argv [linsert $argv 0 "--define" ]
set argv [linsert $argv 1 "__gpg_check_password_cmd /bin/true" ]
set argv [linsert $argv 0 "--define" ]
set argv [linsert $argv 1 "%__gpg_sign_cmd %{__gpg} gpg --batch --no-verbose --no-armor --use-agent --no-secmem-warning -u '%{_gpg_name}' -sbo %{__signature_filename} %{__plaintext_filename}" ]

eval spawn -noecho rpm $argv

set timeout 300

expect {
    "Enter pass phrase:"  { send -- "\r"; exp_continue }
    timeout                 {exp_continue}
    "Pass phrase is good."  {exp_continue}
    eof
}

set status [wait]
exit [lindex $status 3]

