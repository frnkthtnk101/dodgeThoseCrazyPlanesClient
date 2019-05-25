$Data1 = @{
    "Message" = 00001001;
    "Session ID" = 1;
    "Version" = 00001000;
    "Data" = @{
        "Diffculty" = "Hard";
        "PlaneTypes" = ("downers","lefters","righters");
        "CompleteAt" = 1000;
        "level" = (
            @{"tick" = 10; "enemies" = "downers"; "number" =1},
            @{"tick" = 20; "enemies" = "lefters"; "number" =1},
            @{"tick" = 30; "enemies" = "righters"; "number" =1},
            @{"tick" = 40; "enemies" = "downers"; "number" =1},
            @{"tick" = 50; "enemies" = "lefters"; "number" =1},
            @{"tick" = 60; "enemies" = "righters"; "number" =1},
            @{"tick" = 70; "enemies" = "downers"; "number" =1},
            @{"tick" = 80; "enemies" = "lefters"; "number" =1},
            @{"tick" = 90; "enemies" = "righters"; "number" =1},
            @{"tick" = 100; "enemies" = "downers"; "number" =1},
            @{"tick" = 110; "enemies" = "lefters"; "number" =1},
            @{"tick" = 120; "enemies" = "righters"; "number" =1},
            @{"tick" = 130; "enemies" = "downers"; "number" =1},
            @{"tick" = 140; "enemies" = "lefters"; "number" =1},
            @{"tick" = 150; "enemies" = "righters"; "number" =1},
            @{"tick" = 160; "enemies" = "downers"; "number" =1},
            @{"tick" = 170; "enemies" = "lefters"; "number" =1},
            @{"tick" = 180; "enemies" = "righters"; "number" =1},
            @{"tick" = 190; "enemies" = "downers"; "number" =1},
            @{"tick" = 200; "enemies" = "lefters"; "number" =1},
            @{"tick" = 300; "enemies" = "righters"; "number" =1},
            @{"tick" = 310; "enemies" = "downers"; "number" =1},
            @{"tick" = 320; "enemies" = "lefters"; "number" =1},
            @{"tick" = 330; "enemies" = "righters"; "number" =1},
            @{"tick" = 400; "enemies" = "downers"; "number" =1},
            @{"tick" = 500; "enemies" = "lefters"; "number" =1},
            @{"tick" = 600; "enemies" = "righters"; "number" =1},
            @{"tick" = 700; "enemies" = "downers"; "number" =1},
            @{"tick" = 800; "enemies" = "lefters"; "number" =1},
            @{"tick" = 900; "enemies" = "righters"; "number" =1},
            @{"tick" = 901; "enemies" = "downers"; "number" =1},
            @{"tick" = 901; "enemies" = "lefters"; "number" =1},
            @{"tick" = 901; "enemies" = "righters"; "number" =1}


        )
    }

}

<#
	Message: 00001001
	Session ID: 1
	Version: 00001000
	Data: { Difficulty : hard, 
		PlaneTypes : [downers, lefters, righters],
		CompleteAt : 300
		Level : [ {tick: 100, enemies [downers, lefters], number: 10} ,
			 {tick: 150, enemies [downers], number: 10} ,
			 {tick: 200, enemies [lefters], number : 10} ,
			 {tick: 250, enemies [rights], number : 10} ,
			{tick: 299, enemies [downers], number : 1} ] 
		
		}

#>