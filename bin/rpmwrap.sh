#!/usr/bin/expect --

eval spawn -noecho rpm [lrange $argv 0 end]; 

set timeout 300

expect {
    "Enter pass phrase:"  { send -- "\r"; exp_continue }
    timeout                 {exp_continue}
    "Pass phrase is good."  {exp_continue}
    eof
}

set status [wait]
exit [lindex $status 3]
