def do_parentheses_match(input_string):
    s = []
    balanced = True
    index = 0
    while index < len(input_string) and balanced:
        token = input_string[index]
        if token == "{":
            s.append(token)
        elif token == "}":
            if len(s) == 0:
                balanced = False
            else:
                s.pop()

        index += 1

    return balanced and len(s) == 0


text = '''  gamelift_fleets = {
    1 = {
      build_file = "ryanspies-gameserver_linux.zip"
      gamelift_build_name = "${local.title}-${local.env}-${local.aws_region}-build-1"
      gamelift_alias_name = "${local.title}-${local.env}-${local.aws_region}-ON_DEMAND-1"
      gamelift_fleet_type = "ON_DEMAND"
      gamelift_instance_type = "c5.large"
      gamelift_build_version = "1"
      gamelift_fleet_name = "${local.title}_${local.entrypoint}_${local.env}_fleet_ON_DEMAND_1"
      gamelift_game_session_queue_name = "${local.title}-${local.aws_region}-Queue-1"
      fleet-desired-instances = 1
      fleet-max-instances = 1
    }
    2 = {
      build_file = "RyanSpiesGameLift-1.0.0_39_64d9793.zip"
      gamelift_build_name = "${local.title}-${local.env}-${local.aws_region}-build-2"
      gamelift_alias_name = "${local.title}-${local.env}-${local.aws_region}-SPOT-2"
      gamelift_fleet_type = "SPOT"
      gamelift_instance_type = "c5.large"
      gamelift_build_version = "2"
      gamelift_fleet_name = "${local.title}_${local.entrypoint}_${local.env}_fleet_SPOT_2"
      gamelift_game_session_queue_name = "${local.title}-${local.aws_region}-Queue-2"
      fleet-desired-instances = 2
      fleet-max-instances = 3
    }
  }'''

print(do_parentheses_match(text))
