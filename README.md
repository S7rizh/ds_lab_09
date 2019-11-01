# ds_lab_09

![Image 1](https://github.com/S7rizh/ds_lab_09/blob/master/first.png)
```
rs0:PRIMARY> rs.config()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "mongonode1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "mongonode2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "mongonode3:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5dbc94342ac25215a8379f4b")
	}
}
rs0:PRIMARY> rs.status
function() {
    return db._adminCommand("replSetGetStatus");
}
rs0:PRIMARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-11-01T20:47:11.703Z"),
	"myState" : 1,
	"term" : NumberLong(1),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572641227, 1),
			"t" : NumberLong(1)
		},
		"lastCommittedWallTime" : ISODate("2019-11-01T20:47:07.611Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572641227, 1),
			"t" : NumberLong(1)
		},
		"readConcernMajorityWallTime" : ISODate("2019-11-01T20:47:07.611Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572641227, 1),
			"t" : NumberLong(1)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572641227, 1),
			"t" : NumberLong(1)
		},
		"lastAppliedWallTime" : ISODate("2019-11-01T20:47:07.611Z"),
		"lastDurableWallTime" : ISODate("2019-11-01T20:47:07.611Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572641187, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572641187, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "electionTimeout",
		"lastElectionDate" : ISODate("2019-11-01T20:23:26.909Z"),
		"termAtElection" : NumberLong(1),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(0, 0),
			"t" : NumberLong(-1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572639796, 1),
			"t" : NumberLong(-1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-11-01T20:23:27.571Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-11-01T20:23:28.460Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "mongonode1:27017",
			"ip" : "172.31.28.236",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 1435,
			"optime" : {
				"ts" : Timestamp(1572641227, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572641227, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T20:47:07Z"),
			"optimeDurableDate" : ISODate("2019-11-01T20:47:07Z"),
			"lastHeartbeat" : ISODate("2019-11-01T20:47:11.057Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T20:47:10.612Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "mongonode3:27017",
			"syncSourceHost" : "mongonode3:27017",
			"syncSourceId" : 2,
			"infoMessage" : "",
			"configVersion" : 1
		},
		{
			"_id" : 1,
			"name" : "mongonode2:27017",
			"ip" : "172.31.20.144",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 1435,
			"optime" : {
				"ts" : Timestamp(1572641227, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572641227, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T20:47:07Z"),
			"optimeDurableDate" : ISODate("2019-11-01T20:47:07Z"),
			"lastHeartbeat" : ISODate("2019-11-01T20:47:11.056Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T20:47:10.618Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "mongonode3:27017",
			"syncSourceHost" : "mongonode3:27017",
			"syncSourceId" : 2,
			"infoMessage" : "",
			"configVersion" : 1
		},
		{
			"_id" : 2,
			"name" : "mongonode3:27017",
			"ip" : "172.31.16.235",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 1450,
			"optime" : {
				"ts" : Timestamp(1572641227, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T20:47:07Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572639806, 1),
			"electionDate" : ISODate("2019-11-01T20:23:26Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572641227, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572641227, 1)
}
rs0:PRIMARY>
```

# Second iteration
![Image 2](https://github.com/S7rizh/ds_lab_09/blob/master/second.png)
```
rs0:PRIMARY> rs.config()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "mongonode1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "mongonode2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "mongonode3:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5dbc94342ac25215a8379f4b")
	}
}
rs0:PRIMARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-11-01T20:54:04.731Z"),
	"myState" : 1,
	"term" : NumberLong(2),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572641641, 1),
			"t" : NumberLong(2)
		},
		"lastCommittedWallTime" : ISODate("2019-11-01T20:54:01.642Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572641641, 1),
			"t" : NumberLong(2)
		},
		"readConcernMajorityWallTime" : ISODate("2019-11-01T20:54:01.642Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572641641, 1),
			"t" : NumberLong(2)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572641641, 1),
			"t" : NumberLong(2)
		},
		"lastAppliedWallTime" : ISODate("2019-11-01T20:54:01.642Z"),
		"lastDurableWallTime" : ISODate("2019-11-01T20:54:01.642Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572641607, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572641607, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "stepUpRequestSkipDryRun",
		"lastElectionDate" : ISODate("2019-11-01T20:53:30.625Z"),
		"termAtElection" : NumberLong(2),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(1572641607, 1),
			"t" : NumberLong(1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572641607, 1),
			"t" : NumberLong(1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"priorPrimaryMemberId" : 2,
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-11-01T20:53:31.641Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-11-01T20:53:32.832Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "mongonode1:27017",
			"ip" : "172.31.28.236",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 1873,
			"optime" : {
				"ts" : Timestamp(1572641641, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-11-01T20:54:01Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "could not find member to sync from",
			"electionTime" : Timestamp(1572641610, 1),
			"electionDate" : ISODate("2019-11-01T20:53:30Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 1,
			"name" : "mongonode2:27017",
			"ip" : "172.31.20.144",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 1847,
			"optime" : {
				"ts" : Timestamp(1572641641, 1),
				"t" : NumberLong(2)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572641641, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-11-01T20:54:01Z"),
			"optimeDurableDate" : ISODate("2019-11-01T20:54:01Z"),
			"lastHeartbeat" : ISODate("2019-11-01T20:54:04.638Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T20:54:02.831Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "mongonode1:27017",
			"syncSourceHost" : "mongonode1:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		},
		{
			"_id" : 2,
			"name" : "mongonode3:27017",
			"ip" : "172.31.16.235",
			"health" : 0,
			"state" : 8,
			"stateStr" : "(not reachable/healthy)",
			"uptime" : 0,
			"optime" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDate" : ISODate("1970-01-01T00:00:00Z"),
			"optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
			"lastHeartbeat" : ISODate("2019-11-01T20:54:02.920Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T20:53:29.121Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "Error connecting to mongonode3:27017 (172.31.16.235:27017) :: caused by :: Connection refused",
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"configVersion" : -1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572641641, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572641641, 1)
}
rs0:PRIMARY> 
```
