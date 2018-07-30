aws ec2 describe-instances | jq '.Reservations[].Instances | select(.[].Tags[].Value | startswith("Dory Prod") ) |
  select(.[].Tags[].Key == "Name") |
  {InstanceId: .[].InstanceId, PublicDnsName: .[].PublicDnsName, State: .[].State, LaunchTime: .[].LaunchTime, Tags: .[].Tags}
  | [.]' | jq .[].InstanceId
