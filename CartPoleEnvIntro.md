All environments registered in gym:


```python
from gym import envs
print(envs.registry.all())
```

    dict_values([EnvSpec(Copy-v0), EnvSpec(RepeatCopy-v0), EnvSpec(ReversedAddition-v0), EnvSpec(ReversedAddition3-v0), EnvSpec(DuplicatedInput-v0), EnvSpec(Reverse-v0), EnvSpec(CartPole-v0), EnvSpec(CartPole-v1), EnvSpec(MountainCar-v0), EnvSpec(MountainCarContinuous-v0), EnvSpec(Pendulum-v0), EnvSpec(Acrobot-v1), EnvSpec(LunarLander-v2), EnvSpec(LunarLanderContinuous-v2), EnvSpec(BipedalWalker-v3), EnvSpec(BipedalWalkerHardcore-v3), EnvSpec(CarRacing-v0), EnvSpec(Blackjack-v0), EnvSpec(KellyCoinflip-v0), EnvSpec(KellyCoinflipGeneralized-v0), EnvSpec(FrozenLake-v0), EnvSpec(FrozenLake8x8-v0), EnvSpec(CliffWalking-v0), EnvSpec(NChain-v0), EnvSpec(Roulette-v0), EnvSpec(Taxi-v3), EnvSpec(GuessingGame-v0), EnvSpec(HotterColder-v0), EnvSpec(Reacher-v2), EnvSpec(Pusher-v2), EnvSpec(Thrower-v2), EnvSpec(Striker-v2), EnvSpec(InvertedPendulum-v2), EnvSpec(InvertedDoublePendulum-v2), EnvSpec(HalfCheetah-v2), EnvSpec(HalfCheetah-v3), EnvSpec(Hopper-v2), EnvSpec(Hopper-v3), EnvSpec(Swimmer-v2), EnvSpec(Swimmer-v3), EnvSpec(Walker2d-v2), EnvSpec(Walker2d-v3), EnvSpec(Ant-v2), EnvSpec(Ant-v3), EnvSpec(Humanoid-v2), EnvSpec(Humanoid-v3), EnvSpec(HumanoidStandup-v2), EnvSpec(FetchSlide-v1), EnvSpec(FetchPickAndPlace-v1), EnvSpec(FetchReach-v1), EnvSpec(FetchPush-v1), EnvSpec(HandReach-v0), EnvSpec(HandManipulateBlockRotateZ-v0), EnvSpec(HandManipulateBlockRotateZTouchSensors-v0), EnvSpec(HandManipulateBlockRotateZTouchSensors-v1), EnvSpec(HandManipulateBlockRotateParallel-v0), EnvSpec(HandManipulateBlockRotateParallelTouchSensors-v0), EnvSpec(HandManipulateBlockRotateParallelTouchSensors-v1), EnvSpec(HandManipulateBlockRotateXYZ-v0), EnvSpec(HandManipulateBlockRotateXYZTouchSensors-v0), EnvSpec(HandManipulateBlockRotateXYZTouchSensors-v1), EnvSpec(HandManipulateBlockFull-v0), EnvSpec(HandManipulateBlock-v0), EnvSpec(HandManipulateBlockTouchSensors-v0), EnvSpec(HandManipulateBlockTouchSensors-v1), EnvSpec(HandManipulateEggRotate-v0), EnvSpec(HandManipulateEggRotateTouchSensors-v0), EnvSpec(HandManipulateEggRotateTouchSensors-v1), EnvSpec(HandManipulateEggFull-v0), EnvSpec(HandManipulateEgg-v0), EnvSpec(HandManipulateEggTouchSensors-v0), EnvSpec(HandManipulateEggTouchSensors-v1), EnvSpec(HandManipulatePenRotate-v0), EnvSpec(HandManipulatePenRotateTouchSensors-v0), EnvSpec(HandManipulatePenRotateTouchSensors-v1), EnvSpec(HandManipulatePenFull-v0), EnvSpec(HandManipulatePen-v0), EnvSpec(HandManipulatePenTouchSensors-v0), EnvSpec(HandManipulatePenTouchSensors-v1), EnvSpec(FetchSlideDense-v1), EnvSpec(FetchPickAndPlaceDense-v1), EnvSpec(FetchReachDense-v1), EnvSpec(FetchPushDense-v1), EnvSpec(HandReachDense-v0), EnvSpec(HandManipulateBlockRotateZDense-v0), EnvSpec(HandManipulateBlockRotateZTouchSensorsDense-v0), EnvSpec(HandManipulateBlockRotateZTouchSensorsDense-v1), EnvSpec(HandManipulateBlockRotateParallelDense-v0), EnvSpec(HandManipulateBlockRotateParallelTouchSensorsDense-v0), EnvSpec(HandManipulateBlockRotateParallelTouchSensorsDense-v1), EnvSpec(HandManipulateBlockRotateXYZDense-v0), EnvSpec(HandManipulateBlockRotateXYZTouchSensorsDense-v0), EnvSpec(HandManipulateBlockRotateXYZTouchSensorsDense-v1), EnvSpec(HandManipulateBlockFullDense-v0), EnvSpec(HandManipulateBlockDense-v0), EnvSpec(HandManipulateBlockTouchSensorsDense-v0), EnvSpec(HandManipulateBlockTouchSensorsDense-v1), EnvSpec(HandManipulateEggRotateDense-v0), EnvSpec(HandManipulateEggRotateTouchSensorsDense-v0), EnvSpec(HandManipulateEggRotateTouchSensorsDense-v1), EnvSpec(HandManipulateEggFullDense-v0), EnvSpec(HandManipulateEggDense-v0), EnvSpec(HandManipulateEggTouchSensorsDense-v0), EnvSpec(HandManipulateEggTouchSensorsDense-v1), EnvSpec(HandManipulatePenRotateDense-v0), EnvSpec(HandManipulatePenRotateTouchSensorsDense-v0), EnvSpec(HandManipulatePenRotateTouchSensorsDense-v1), EnvSpec(HandManipulatePenFullDense-v0), EnvSpec(HandManipulatePenDense-v0), EnvSpec(HandManipulatePenTouchSensorsDense-v0), EnvSpec(HandManipulatePenTouchSensorsDense-v1), EnvSpec(Adventure-v0), EnvSpec(Adventure-v4), EnvSpec(AdventureDeterministic-v0), EnvSpec(AdventureDeterministic-v4), EnvSpec(AdventureNoFrameskip-v0), EnvSpec(AdventureNoFrameskip-v4), EnvSpec(Adventure-ram-v0), EnvSpec(Adventure-ram-v4), EnvSpec(Adventure-ramDeterministic-v0), EnvSpec(Adventure-ramDeterministic-v4), EnvSpec(Adventure-ramNoFrameskip-v0), EnvSpec(Adventure-ramNoFrameskip-v4), EnvSpec(AirRaid-v0), EnvSpec(AirRaid-v4), EnvSpec(AirRaidDeterministic-v0), EnvSpec(AirRaidDeterministic-v4), EnvSpec(AirRaidNoFrameskip-v0), EnvSpec(AirRaidNoFrameskip-v4), EnvSpec(AirRaid-ram-v0), EnvSpec(AirRaid-ram-v4), EnvSpec(AirRaid-ramDeterministic-v0), EnvSpec(AirRaid-ramDeterministic-v4), EnvSpec(AirRaid-ramNoFrameskip-v0), EnvSpec(AirRaid-ramNoFrameskip-v4), EnvSpec(Alien-v0), EnvSpec(Alien-v4), EnvSpec(AlienDeterministic-v0), EnvSpec(AlienDeterministic-v4), EnvSpec(AlienNoFrameskip-v0), EnvSpec(AlienNoFrameskip-v4), EnvSpec(Alien-ram-v0), EnvSpec(Alien-ram-v4), EnvSpec(Alien-ramDeterministic-v0), EnvSpec(Alien-ramDeterministic-v4), EnvSpec(Alien-ramNoFrameskip-v0), EnvSpec(Alien-ramNoFrameskip-v4), EnvSpec(Amidar-v0), EnvSpec(Amidar-v4), EnvSpec(AmidarDeterministic-v0), EnvSpec(AmidarDeterministic-v4), EnvSpec(AmidarNoFrameskip-v0), EnvSpec(AmidarNoFrameskip-v4), EnvSpec(Amidar-ram-v0), EnvSpec(Amidar-ram-v4), EnvSpec(Amidar-ramDeterministic-v0), EnvSpec(Amidar-ramDeterministic-v4), EnvSpec(Amidar-ramNoFrameskip-v0), EnvSpec(Amidar-ramNoFrameskip-v4), EnvSpec(Assault-v0), EnvSpec(Assault-v4), EnvSpec(AssaultDeterministic-v0), EnvSpec(AssaultDeterministic-v4), EnvSpec(AssaultNoFrameskip-v0), EnvSpec(AssaultNoFrameskip-v4), EnvSpec(Assault-ram-v0), EnvSpec(Assault-ram-v4), EnvSpec(Assault-ramDeterministic-v0), EnvSpec(Assault-ramDeterministic-v4), EnvSpec(Assault-ramNoFrameskip-v0), EnvSpec(Assault-ramNoFrameskip-v4), EnvSpec(Asterix-v0), EnvSpec(Asterix-v4), EnvSpec(AsterixDeterministic-v0), EnvSpec(AsterixDeterministic-v4), EnvSpec(AsterixNoFrameskip-v0), EnvSpec(AsterixNoFrameskip-v4), EnvSpec(Asterix-ram-v0), EnvSpec(Asterix-ram-v4), EnvSpec(Asterix-ramDeterministic-v0), EnvSpec(Asterix-ramDeterministic-v4), EnvSpec(Asterix-ramNoFrameskip-v0), EnvSpec(Asterix-ramNoFrameskip-v4), EnvSpec(Asteroids-v0), EnvSpec(Asteroids-v4), EnvSpec(AsteroidsDeterministic-v0), EnvSpec(AsteroidsDeterministic-v4), EnvSpec(AsteroidsNoFrameskip-v0), EnvSpec(AsteroidsNoFrameskip-v4), EnvSpec(Asteroids-ram-v0), EnvSpec(Asteroids-ram-v4), EnvSpec(Asteroids-ramDeterministic-v0), EnvSpec(Asteroids-ramDeterministic-v4), EnvSpec(Asteroids-ramNoFrameskip-v0), EnvSpec(Asteroids-ramNoFrameskip-v4), EnvSpec(Atlantis-v0), EnvSpec(Atlantis-v4), EnvSpec(AtlantisDeterministic-v0), EnvSpec(AtlantisDeterministic-v4), EnvSpec(AtlantisNoFrameskip-v0), EnvSpec(AtlantisNoFrameskip-v4), EnvSpec(Atlantis-ram-v0), EnvSpec(Atlantis-ram-v4), EnvSpec(Atlantis-ramDeterministic-v0), EnvSpec(Atlantis-ramDeterministic-v4), EnvSpec(Atlantis-ramNoFrameskip-v0), EnvSpec(Atlantis-ramNoFrameskip-v4), EnvSpec(BankHeist-v0), EnvSpec(BankHeist-v4), EnvSpec(BankHeistDeterministic-v0), EnvSpec(BankHeistDeterministic-v4), EnvSpec(BankHeistNoFrameskip-v0), EnvSpec(BankHeistNoFrameskip-v4), EnvSpec(BankHeist-ram-v0), EnvSpec(BankHeist-ram-v4), EnvSpec(BankHeist-ramDeterministic-v0), EnvSpec(BankHeist-ramDeterministic-v4), EnvSpec(BankHeist-ramNoFrameskip-v0), EnvSpec(BankHeist-ramNoFrameskip-v4), EnvSpec(BattleZone-v0), EnvSpec(BattleZone-v4), EnvSpec(BattleZoneDeterministic-v0), EnvSpec(BattleZoneDeterministic-v4), EnvSpec(BattleZoneNoFrameskip-v0), EnvSpec(BattleZoneNoFrameskip-v4), EnvSpec(BattleZone-ram-v0), EnvSpec(BattleZone-ram-v4), EnvSpec(BattleZone-ramDeterministic-v0), EnvSpec(BattleZone-ramDeterministic-v4), EnvSpec(BattleZone-ramNoFrameskip-v0), EnvSpec(BattleZone-ramNoFrameskip-v4), EnvSpec(BeamRider-v0), EnvSpec(BeamRider-v4), EnvSpec(BeamRiderDeterministic-v0), EnvSpec(BeamRiderDeterministic-v4), EnvSpec(BeamRiderNoFrameskip-v0), EnvSpec(BeamRiderNoFrameskip-v4), EnvSpec(BeamRider-ram-v0), EnvSpec(BeamRider-ram-v4), EnvSpec(BeamRider-ramDeterministic-v0), EnvSpec(BeamRider-ramDeterministic-v4), EnvSpec(BeamRider-ramNoFrameskip-v0), EnvSpec(BeamRider-ramNoFrameskip-v4), EnvSpec(Berzerk-v0), EnvSpec(Berzerk-v4), EnvSpec(BerzerkDeterministic-v0), EnvSpec(BerzerkDeterministic-v4), EnvSpec(BerzerkNoFrameskip-v0), EnvSpec(BerzerkNoFrameskip-v4), EnvSpec(Berzerk-ram-v0), EnvSpec(Berzerk-ram-v4), EnvSpec(Berzerk-ramDeterministic-v0), EnvSpec(Berzerk-ramDeterministic-v4), EnvSpec(Berzerk-ramNoFrameskip-v0), EnvSpec(Berzerk-ramNoFrameskip-v4), EnvSpec(Bowling-v0), EnvSpec(Bowling-v4), EnvSpec(BowlingDeterministic-v0), EnvSpec(BowlingDeterministic-v4), EnvSpec(BowlingNoFrameskip-v0), EnvSpec(BowlingNoFrameskip-v4), EnvSpec(Bowling-ram-v0), EnvSpec(Bowling-ram-v4), EnvSpec(Bowling-ramDeterministic-v0), EnvSpec(Bowling-ramDeterministic-v4), EnvSpec(Bowling-ramNoFrameskip-v0), EnvSpec(Bowling-ramNoFrameskip-v4), EnvSpec(Boxing-v0), EnvSpec(Boxing-v4), EnvSpec(BoxingDeterministic-v0), EnvSpec(BoxingDeterministic-v4), EnvSpec(BoxingNoFrameskip-v0), EnvSpec(BoxingNoFrameskip-v4), EnvSpec(Boxing-ram-v0), EnvSpec(Boxing-ram-v4), EnvSpec(Boxing-ramDeterministic-v0), EnvSpec(Boxing-ramDeterministic-v4), EnvSpec(Boxing-ramNoFrameskip-v0), EnvSpec(Boxing-ramNoFrameskip-v4), EnvSpec(Breakout-v0), EnvSpec(Breakout-v4), EnvSpec(BreakoutDeterministic-v0), EnvSpec(BreakoutDeterministic-v4), EnvSpec(BreakoutNoFrameskip-v0), EnvSpec(BreakoutNoFrameskip-v4), EnvSpec(Breakout-ram-v0), EnvSpec(Breakout-ram-v4), EnvSpec(Breakout-ramDeterministic-v0), EnvSpec(Breakout-ramDeterministic-v4), EnvSpec(Breakout-ramNoFrameskip-v0), EnvSpec(Breakout-ramNoFrameskip-v4), EnvSpec(Carnival-v0), EnvSpec(Carnival-v4), EnvSpec(CarnivalDeterministic-v0), EnvSpec(CarnivalDeterministic-v4), EnvSpec(CarnivalNoFrameskip-v0), EnvSpec(CarnivalNoFrameskip-v4), EnvSpec(Carnival-ram-v0), EnvSpec(Carnival-ram-v4), EnvSpec(Carnival-ramDeterministic-v0), EnvSpec(Carnival-ramDeterministic-v4), EnvSpec(Carnival-ramNoFrameskip-v0), EnvSpec(Carnival-ramNoFrameskip-v4), EnvSpec(Centipede-v0), EnvSpec(Centipede-v4), EnvSpec(CentipedeDeterministic-v0), EnvSpec(CentipedeDeterministic-v4), EnvSpec(CentipedeNoFrameskip-v0), EnvSpec(CentipedeNoFrameskip-v4), EnvSpec(Centipede-ram-v0), EnvSpec(Centipede-ram-v4), EnvSpec(Centipede-ramDeterministic-v0), EnvSpec(Centipede-ramDeterministic-v4), EnvSpec(Centipede-ramNoFrameskip-v0), EnvSpec(Centipede-ramNoFrameskip-v4), EnvSpec(ChopperCommand-v0), EnvSpec(ChopperCommand-v4), EnvSpec(ChopperCommandDeterministic-v0), EnvSpec(ChopperCommandDeterministic-v4), EnvSpec(ChopperCommandNoFrameskip-v0), EnvSpec(ChopperCommandNoFrameskip-v4), EnvSpec(ChopperCommand-ram-v0), EnvSpec(ChopperCommand-ram-v4), EnvSpec(ChopperCommand-ramDeterministic-v0), EnvSpec(ChopperCommand-ramDeterministic-v4), EnvSpec(ChopperCommand-ramNoFrameskip-v0), EnvSpec(ChopperCommand-ramNoFrameskip-v4), EnvSpec(CrazyClimber-v0), EnvSpec(CrazyClimber-v4), EnvSpec(CrazyClimberDeterministic-v0), EnvSpec(CrazyClimberDeterministic-v4), EnvSpec(CrazyClimberNoFrameskip-v0), EnvSpec(CrazyClimberNoFrameskip-v4), EnvSpec(CrazyClimber-ram-v0), EnvSpec(CrazyClimber-ram-v4), EnvSpec(CrazyClimber-ramDeterministic-v0), EnvSpec(CrazyClimber-ramDeterministic-v4), EnvSpec(CrazyClimber-ramNoFrameskip-v0), EnvSpec(CrazyClimber-ramNoFrameskip-v4), EnvSpec(Defender-v0), EnvSpec(Defender-v4), EnvSpec(DefenderDeterministic-v0), EnvSpec(DefenderDeterministic-v4), EnvSpec(DefenderNoFrameskip-v0), EnvSpec(DefenderNoFrameskip-v4), EnvSpec(Defender-ram-v0), EnvSpec(Defender-ram-v4), EnvSpec(Defender-ramDeterministic-v0), EnvSpec(Defender-ramDeterministic-v4), EnvSpec(Defender-ramNoFrameskip-v0), EnvSpec(Defender-ramNoFrameskip-v4), EnvSpec(DemonAttack-v0), EnvSpec(DemonAttack-v4), EnvSpec(DemonAttackDeterministic-v0), EnvSpec(DemonAttackDeterministic-v4), EnvSpec(DemonAttackNoFrameskip-v0), EnvSpec(DemonAttackNoFrameskip-v4), EnvSpec(DemonAttack-ram-v0), EnvSpec(DemonAttack-ram-v4), EnvSpec(DemonAttack-ramDeterministic-v0), EnvSpec(DemonAttack-ramDeterministic-v4), EnvSpec(DemonAttack-ramNoFrameskip-v0), EnvSpec(DemonAttack-ramNoFrameskip-v4), EnvSpec(DoubleDunk-v0), EnvSpec(DoubleDunk-v4), EnvSpec(DoubleDunkDeterministic-v0), EnvSpec(DoubleDunkDeterministic-v4), EnvSpec(DoubleDunkNoFrameskip-v0), EnvSpec(DoubleDunkNoFrameskip-v4), EnvSpec(DoubleDunk-ram-v0), EnvSpec(DoubleDunk-ram-v4), EnvSpec(DoubleDunk-ramDeterministic-v0), EnvSpec(DoubleDunk-ramDeterministic-v4), EnvSpec(DoubleDunk-ramNoFrameskip-v0), EnvSpec(DoubleDunk-ramNoFrameskip-v4), EnvSpec(ElevatorAction-v0), EnvSpec(ElevatorAction-v4), EnvSpec(ElevatorActionDeterministic-v0), EnvSpec(ElevatorActionDeterministic-v4), EnvSpec(ElevatorActionNoFrameskip-v0), EnvSpec(ElevatorActionNoFrameskip-v4), EnvSpec(ElevatorAction-ram-v0), EnvSpec(ElevatorAction-ram-v4), EnvSpec(ElevatorAction-ramDeterministic-v0), EnvSpec(ElevatorAction-ramDeterministic-v4), EnvSpec(ElevatorAction-ramNoFrameskip-v0), EnvSpec(ElevatorAction-ramNoFrameskip-v4), EnvSpec(Enduro-v0), EnvSpec(Enduro-v4), EnvSpec(EnduroDeterministic-v0), EnvSpec(EnduroDeterministic-v4), EnvSpec(EnduroNoFrameskip-v0), EnvSpec(EnduroNoFrameskip-v4), EnvSpec(Enduro-ram-v0), EnvSpec(Enduro-ram-v4), EnvSpec(Enduro-ramDeterministic-v0), EnvSpec(Enduro-ramDeterministic-v4), EnvSpec(Enduro-ramNoFrameskip-v0), EnvSpec(Enduro-ramNoFrameskip-v4), EnvSpec(FishingDerby-v0), EnvSpec(FishingDerby-v4), EnvSpec(FishingDerbyDeterministic-v0), EnvSpec(FishingDerbyDeterministic-v4), EnvSpec(FishingDerbyNoFrameskip-v0), EnvSpec(FishingDerbyNoFrameskip-v4), EnvSpec(FishingDerby-ram-v0), EnvSpec(FishingDerby-ram-v4), EnvSpec(FishingDerby-ramDeterministic-v0), EnvSpec(FishingDerby-ramDeterministic-v4), EnvSpec(FishingDerby-ramNoFrameskip-v0), EnvSpec(FishingDerby-ramNoFrameskip-v4), EnvSpec(Freeway-v0), EnvSpec(Freeway-v4), EnvSpec(FreewayDeterministic-v0), EnvSpec(FreewayDeterministic-v4), EnvSpec(FreewayNoFrameskip-v0), EnvSpec(FreewayNoFrameskip-v4), EnvSpec(Freeway-ram-v0), EnvSpec(Freeway-ram-v4), EnvSpec(Freeway-ramDeterministic-v0), EnvSpec(Freeway-ramDeterministic-v4), EnvSpec(Freeway-ramNoFrameskip-v0), EnvSpec(Freeway-ramNoFrameskip-v4), EnvSpec(Frostbite-v0), EnvSpec(Frostbite-v4), EnvSpec(FrostbiteDeterministic-v0), EnvSpec(FrostbiteDeterministic-v4), EnvSpec(FrostbiteNoFrameskip-v0), EnvSpec(FrostbiteNoFrameskip-v4), EnvSpec(Frostbite-ram-v0), EnvSpec(Frostbite-ram-v4), EnvSpec(Frostbite-ramDeterministic-v0), EnvSpec(Frostbite-ramDeterministic-v4), EnvSpec(Frostbite-ramNoFrameskip-v0), EnvSpec(Frostbite-ramNoFrameskip-v4), EnvSpec(Gopher-v0), EnvSpec(Gopher-v4), EnvSpec(GopherDeterministic-v0), EnvSpec(GopherDeterministic-v4), EnvSpec(GopherNoFrameskip-v0), EnvSpec(GopherNoFrameskip-v4), EnvSpec(Gopher-ram-v0), EnvSpec(Gopher-ram-v4), EnvSpec(Gopher-ramDeterministic-v0), EnvSpec(Gopher-ramDeterministic-v4), EnvSpec(Gopher-ramNoFrameskip-v0), EnvSpec(Gopher-ramNoFrameskip-v4), EnvSpec(Gravitar-v0), EnvSpec(Gravitar-v4), EnvSpec(GravitarDeterministic-v0), EnvSpec(GravitarDeterministic-v4), EnvSpec(GravitarNoFrameskip-v0), EnvSpec(GravitarNoFrameskip-v4), EnvSpec(Gravitar-ram-v0), EnvSpec(Gravitar-ram-v4), EnvSpec(Gravitar-ramDeterministic-v0), EnvSpec(Gravitar-ramDeterministic-v4), EnvSpec(Gravitar-ramNoFrameskip-v0), EnvSpec(Gravitar-ramNoFrameskip-v4), EnvSpec(Hero-v0), EnvSpec(Hero-v4), EnvSpec(HeroDeterministic-v0), EnvSpec(HeroDeterministic-v4), EnvSpec(HeroNoFrameskip-v0), EnvSpec(HeroNoFrameskip-v4), EnvSpec(Hero-ram-v0), EnvSpec(Hero-ram-v4), EnvSpec(Hero-ramDeterministic-v0), EnvSpec(Hero-ramDeterministic-v4), EnvSpec(Hero-ramNoFrameskip-v0), EnvSpec(Hero-ramNoFrameskip-v4), EnvSpec(IceHockey-v0), EnvSpec(IceHockey-v4), EnvSpec(IceHockeyDeterministic-v0), EnvSpec(IceHockeyDeterministic-v4), EnvSpec(IceHockeyNoFrameskip-v0), EnvSpec(IceHockeyNoFrameskip-v4), EnvSpec(IceHockey-ram-v0), EnvSpec(IceHockey-ram-v4), EnvSpec(IceHockey-ramDeterministic-v0), EnvSpec(IceHockey-ramDeterministic-v4), EnvSpec(IceHockey-ramNoFrameskip-v0), EnvSpec(IceHockey-ramNoFrameskip-v4), EnvSpec(Jamesbond-v0), EnvSpec(Jamesbond-v4), EnvSpec(JamesbondDeterministic-v0), EnvSpec(JamesbondDeterministic-v4), EnvSpec(JamesbondNoFrameskip-v0), EnvSpec(JamesbondNoFrameskip-v4), EnvSpec(Jamesbond-ram-v0), EnvSpec(Jamesbond-ram-v4), EnvSpec(Jamesbond-ramDeterministic-v0), EnvSpec(Jamesbond-ramDeterministic-v4), EnvSpec(Jamesbond-ramNoFrameskip-v0), EnvSpec(Jamesbond-ramNoFrameskip-v4), EnvSpec(JourneyEscape-v0), EnvSpec(JourneyEscape-v4), EnvSpec(JourneyEscapeDeterministic-v0), EnvSpec(JourneyEscapeDeterministic-v4), EnvSpec(JourneyEscapeNoFrameskip-v0), EnvSpec(JourneyEscapeNoFrameskip-v4), EnvSpec(JourneyEscape-ram-v0), EnvSpec(JourneyEscape-ram-v4), EnvSpec(JourneyEscape-ramDeterministic-v0), EnvSpec(JourneyEscape-ramDeterministic-v4), EnvSpec(JourneyEscape-ramNoFrameskip-v0), EnvSpec(JourneyEscape-ramNoFrameskip-v4), EnvSpec(Kangaroo-v0), EnvSpec(Kangaroo-v4), EnvSpec(KangarooDeterministic-v0), EnvSpec(KangarooDeterministic-v4), EnvSpec(KangarooNoFrameskip-v0), EnvSpec(KangarooNoFrameskip-v4), EnvSpec(Kangaroo-ram-v0), EnvSpec(Kangaroo-ram-v4), EnvSpec(Kangaroo-ramDeterministic-v0), EnvSpec(Kangaroo-ramDeterministic-v4), EnvSpec(Kangaroo-ramNoFrameskip-v0), EnvSpec(Kangaroo-ramNoFrameskip-v4), EnvSpec(Krull-v0), EnvSpec(Krull-v4), EnvSpec(KrullDeterministic-v0), EnvSpec(KrullDeterministic-v4), EnvSpec(KrullNoFrameskip-v0), EnvSpec(KrullNoFrameskip-v4), EnvSpec(Krull-ram-v0), EnvSpec(Krull-ram-v4), EnvSpec(Krull-ramDeterministic-v0), EnvSpec(Krull-ramDeterministic-v4), EnvSpec(Krull-ramNoFrameskip-v0), EnvSpec(Krull-ramNoFrameskip-v4), EnvSpec(KungFuMaster-v0), EnvSpec(KungFuMaster-v4), EnvSpec(KungFuMasterDeterministic-v0), EnvSpec(KungFuMasterDeterministic-v4), EnvSpec(KungFuMasterNoFrameskip-v0), EnvSpec(KungFuMasterNoFrameskip-v4), EnvSpec(KungFuMaster-ram-v0), EnvSpec(KungFuMaster-ram-v4), EnvSpec(KungFuMaster-ramDeterministic-v0), EnvSpec(KungFuMaster-ramDeterministic-v4), EnvSpec(KungFuMaster-ramNoFrameskip-v0), EnvSpec(KungFuMaster-ramNoFrameskip-v4), EnvSpec(MontezumaRevenge-v0), EnvSpec(MontezumaRevenge-v4), EnvSpec(MontezumaRevengeDeterministic-v0), EnvSpec(MontezumaRevengeDeterministic-v4), EnvSpec(MontezumaRevengeNoFrameskip-v0), EnvSpec(MontezumaRevengeNoFrameskip-v4), EnvSpec(MontezumaRevenge-ram-v0), EnvSpec(MontezumaRevenge-ram-v4), EnvSpec(MontezumaRevenge-ramDeterministic-v0), EnvSpec(MontezumaRevenge-ramDeterministic-v4), EnvSpec(MontezumaRevenge-ramNoFrameskip-v0), EnvSpec(MontezumaRevenge-ramNoFrameskip-v4), EnvSpec(MsPacman-v0), EnvSpec(MsPacman-v4), EnvSpec(MsPacmanDeterministic-v0), EnvSpec(MsPacmanDeterministic-v4), EnvSpec(MsPacmanNoFrameskip-v0), EnvSpec(MsPacmanNoFrameskip-v4), EnvSpec(MsPacman-ram-v0), EnvSpec(MsPacman-ram-v4), EnvSpec(MsPacman-ramDeterministic-v0), EnvSpec(MsPacman-ramDeterministic-v4), EnvSpec(MsPacman-ramNoFrameskip-v0), EnvSpec(MsPacman-ramNoFrameskip-v4), EnvSpec(NameThisGame-v0), EnvSpec(NameThisGame-v4), EnvSpec(NameThisGameDeterministic-v0), EnvSpec(NameThisGameDeterministic-v4), EnvSpec(NameThisGameNoFrameskip-v0), EnvSpec(NameThisGameNoFrameskip-v4), EnvSpec(NameThisGame-ram-v0), EnvSpec(NameThisGame-ram-v4), EnvSpec(NameThisGame-ramDeterministic-v0), EnvSpec(NameThisGame-ramDeterministic-v4), EnvSpec(NameThisGame-ramNoFrameskip-v0), EnvSpec(NameThisGame-ramNoFrameskip-v4), EnvSpec(Phoenix-v0), EnvSpec(Phoenix-v4), EnvSpec(PhoenixDeterministic-v0), EnvSpec(PhoenixDeterministic-v4), EnvSpec(PhoenixNoFrameskip-v0), EnvSpec(PhoenixNoFrameskip-v4), EnvSpec(Phoenix-ram-v0), EnvSpec(Phoenix-ram-v4), EnvSpec(Phoenix-ramDeterministic-v0), EnvSpec(Phoenix-ramDeterministic-v4), EnvSpec(Phoenix-ramNoFrameskip-v0), EnvSpec(Phoenix-ramNoFrameskip-v4), EnvSpec(Pitfall-v0), EnvSpec(Pitfall-v4), EnvSpec(PitfallDeterministic-v0), EnvSpec(PitfallDeterministic-v4), EnvSpec(PitfallNoFrameskip-v0), EnvSpec(PitfallNoFrameskip-v4), EnvSpec(Pitfall-ram-v0), EnvSpec(Pitfall-ram-v4), EnvSpec(Pitfall-ramDeterministic-v0), EnvSpec(Pitfall-ramDeterministic-v4), EnvSpec(Pitfall-ramNoFrameskip-v0), EnvSpec(Pitfall-ramNoFrameskip-v4), EnvSpec(Pong-v0), EnvSpec(Pong-v4), EnvSpec(PongDeterministic-v0), EnvSpec(PongDeterministic-v4), EnvSpec(PongNoFrameskip-v0), EnvSpec(PongNoFrameskip-v4), EnvSpec(Pong-ram-v0), EnvSpec(Pong-ram-v4), EnvSpec(Pong-ramDeterministic-v0), EnvSpec(Pong-ramDeterministic-v4), EnvSpec(Pong-ramNoFrameskip-v0), EnvSpec(Pong-ramNoFrameskip-v4), EnvSpec(Pooyan-v0), EnvSpec(Pooyan-v4), EnvSpec(PooyanDeterministic-v0), EnvSpec(PooyanDeterministic-v4), EnvSpec(PooyanNoFrameskip-v0), EnvSpec(PooyanNoFrameskip-v4), EnvSpec(Pooyan-ram-v0), EnvSpec(Pooyan-ram-v4), EnvSpec(Pooyan-ramDeterministic-v0), EnvSpec(Pooyan-ramDeterministic-v4), EnvSpec(Pooyan-ramNoFrameskip-v0), EnvSpec(Pooyan-ramNoFrameskip-v4), EnvSpec(PrivateEye-v0), EnvSpec(PrivateEye-v4), EnvSpec(PrivateEyeDeterministic-v0), EnvSpec(PrivateEyeDeterministic-v4), EnvSpec(PrivateEyeNoFrameskip-v0), EnvSpec(PrivateEyeNoFrameskip-v4), EnvSpec(PrivateEye-ram-v0), EnvSpec(PrivateEye-ram-v4), EnvSpec(PrivateEye-ramDeterministic-v0), EnvSpec(PrivateEye-ramDeterministic-v4), EnvSpec(PrivateEye-ramNoFrameskip-v0), EnvSpec(PrivateEye-ramNoFrameskip-v4), EnvSpec(Qbert-v0), EnvSpec(Qbert-v4), EnvSpec(QbertDeterministic-v0), EnvSpec(QbertDeterministic-v4), EnvSpec(QbertNoFrameskip-v0), EnvSpec(QbertNoFrameskip-v4), EnvSpec(Qbert-ram-v0), EnvSpec(Qbert-ram-v4), EnvSpec(Qbert-ramDeterministic-v0), EnvSpec(Qbert-ramDeterministic-v4), EnvSpec(Qbert-ramNoFrameskip-v0), EnvSpec(Qbert-ramNoFrameskip-v4), EnvSpec(Riverraid-v0), EnvSpec(Riverraid-v4), EnvSpec(RiverraidDeterministic-v0), EnvSpec(RiverraidDeterministic-v4), EnvSpec(RiverraidNoFrameskip-v0), EnvSpec(RiverraidNoFrameskip-v4), EnvSpec(Riverraid-ram-v0), EnvSpec(Riverraid-ram-v4), EnvSpec(Riverraid-ramDeterministic-v0), EnvSpec(Riverraid-ramDeterministic-v4), EnvSpec(Riverraid-ramNoFrameskip-v0), EnvSpec(Riverraid-ramNoFrameskip-v4), EnvSpec(RoadRunner-v0), EnvSpec(RoadRunner-v4), EnvSpec(RoadRunnerDeterministic-v0), EnvSpec(RoadRunnerDeterministic-v4), EnvSpec(RoadRunnerNoFrameskip-v0), EnvSpec(RoadRunnerNoFrameskip-v4), EnvSpec(RoadRunner-ram-v0), EnvSpec(RoadRunner-ram-v4), EnvSpec(RoadRunner-ramDeterministic-v0), EnvSpec(RoadRunner-ramDeterministic-v4), EnvSpec(RoadRunner-ramNoFrameskip-v0), EnvSpec(RoadRunner-ramNoFrameskip-v4), EnvSpec(Robotank-v0), EnvSpec(Robotank-v4), EnvSpec(RobotankDeterministic-v0), EnvSpec(RobotankDeterministic-v4), EnvSpec(RobotankNoFrameskip-v0), EnvSpec(RobotankNoFrameskip-v4), EnvSpec(Robotank-ram-v0), EnvSpec(Robotank-ram-v4), EnvSpec(Robotank-ramDeterministic-v0), EnvSpec(Robotank-ramDeterministic-v4), EnvSpec(Robotank-ramNoFrameskip-v0), EnvSpec(Robotank-ramNoFrameskip-v4), EnvSpec(Seaquest-v0), EnvSpec(Seaquest-v4), EnvSpec(SeaquestDeterministic-v0), EnvSpec(SeaquestDeterministic-v4), EnvSpec(SeaquestNoFrameskip-v0), EnvSpec(SeaquestNoFrameskip-v4), EnvSpec(Seaquest-ram-v0), EnvSpec(Seaquest-ram-v4), EnvSpec(Seaquest-ramDeterministic-v0), EnvSpec(Seaquest-ramDeterministic-v4), EnvSpec(Seaquest-ramNoFrameskip-v0), EnvSpec(Seaquest-ramNoFrameskip-v4), EnvSpec(Skiing-v0), EnvSpec(Skiing-v4), EnvSpec(SkiingDeterministic-v0), EnvSpec(SkiingDeterministic-v4), EnvSpec(SkiingNoFrameskip-v0), EnvSpec(SkiingNoFrameskip-v4), EnvSpec(Skiing-ram-v0), EnvSpec(Skiing-ram-v4), EnvSpec(Skiing-ramDeterministic-v0), EnvSpec(Skiing-ramDeterministic-v4), EnvSpec(Skiing-ramNoFrameskip-v0), EnvSpec(Skiing-ramNoFrameskip-v4), EnvSpec(Solaris-v0), EnvSpec(Solaris-v4), EnvSpec(SolarisDeterministic-v0), EnvSpec(SolarisDeterministic-v4), EnvSpec(SolarisNoFrameskip-v0), EnvSpec(SolarisNoFrameskip-v4), EnvSpec(Solaris-ram-v0), EnvSpec(Solaris-ram-v4), EnvSpec(Solaris-ramDeterministic-v0), EnvSpec(Solaris-ramDeterministic-v4), EnvSpec(Solaris-ramNoFrameskip-v0), EnvSpec(Solaris-ramNoFrameskip-v4), EnvSpec(SpaceInvaders-v0), EnvSpec(SpaceInvaders-v4), EnvSpec(SpaceInvadersDeterministic-v0), EnvSpec(SpaceInvadersDeterministic-v4), EnvSpec(SpaceInvadersNoFrameskip-v0), EnvSpec(SpaceInvadersNoFrameskip-v4), EnvSpec(SpaceInvaders-ram-v0), EnvSpec(SpaceInvaders-ram-v4), EnvSpec(SpaceInvaders-ramDeterministic-v0), EnvSpec(SpaceInvaders-ramDeterministic-v4), EnvSpec(SpaceInvaders-ramNoFrameskip-v0), EnvSpec(SpaceInvaders-ramNoFrameskip-v4), EnvSpec(StarGunner-v0), EnvSpec(StarGunner-v4), EnvSpec(StarGunnerDeterministic-v0), EnvSpec(StarGunnerDeterministic-v4), EnvSpec(StarGunnerNoFrameskip-v0), EnvSpec(StarGunnerNoFrameskip-v4), EnvSpec(StarGunner-ram-v0), EnvSpec(StarGunner-ram-v4), EnvSpec(StarGunner-ramDeterministic-v0), EnvSpec(StarGunner-ramDeterministic-v4), EnvSpec(StarGunner-ramNoFrameskip-v0), EnvSpec(StarGunner-ramNoFrameskip-v4), EnvSpec(Tennis-v0), EnvSpec(Tennis-v4), EnvSpec(TennisDeterministic-v0), EnvSpec(TennisDeterministic-v4), EnvSpec(TennisNoFrameskip-v0), EnvSpec(TennisNoFrameskip-v4), EnvSpec(Tennis-ram-v0), EnvSpec(Tennis-ram-v4), EnvSpec(Tennis-ramDeterministic-v0), EnvSpec(Tennis-ramDeterministic-v4), EnvSpec(Tennis-ramNoFrameskip-v0), EnvSpec(Tennis-ramNoFrameskip-v4), EnvSpec(TimePilot-v0), EnvSpec(TimePilot-v4), EnvSpec(TimePilotDeterministic-v0), EnvSpec(TimePilotDeterministic-v4), EnvSpec(TimePilotNoFrameskip-v0), EnvSpec(TimePilotNoFrameskip-v4), EnvSpec(TimePilot-ram-v0), EnvSpec(TimePilot-ram-v4), EnvSpec(TimePilot-ramDeterministic-v0), EnvSpec(TimePilot-ramDeterministic-v4), EnvSpec(TimePilot-ramNoFrameskip-v0), EnvSpec(TimePilot-ramNoFrameskip-v4), EnvSpec(Tutankham-v0), EnvSpec(Tutankham-v4), EnvSpec(TutankhamDeterministic-v0), EnvSpec(TutankhamDeterministic-v4), EnvSpec(TutankhamNoFrameskip-v0), EnvSpec(TutankhamNoFrameskip-v4), EnvSpec(Tutankham-ram-v0), EnvSpec(Tutankham-ram-v4), EnvSpec(Tutankham-ramDeterministic-v0), EnvSpec(Tutankham-ramDeterministic-v4), EnvSpec(Tutankham-ramNoFrameskip-v0), EnvSpec(Tutankham-ramNoFrameskip-v4), EnvSpec(UpNDown-v0), EnvSpec(UpNDown-v4), EnvSpec(UpNDownDeterministic-v0), EnvSpec(UpNDownDeterministic-v4), EnvSpec(UpNDownNoFrameskip-v0), EnvSpec(UpNDownNoFrameskip-v4), EnvSpec(UpNDown-ram-v0), EnvSpec(UpNDown-ram-v4), EnvSpec(UpNDown-ramDeterministic-v0), EnvSpec(UpNDown-ramDeterministic-v4), EnvSpec(UpNDown-ramNoFrameskip-v0), EnvSpec(UpNDown-ramNoFrameskip-v4), EnvSpec(Venture-v0), EnvSpec(Venture-v4), EnvSpec(VentureDeterministic-v0), EnvSpec(VentureDeterministic-v4), EnvSpec(VentureNoFrameskip-v0), EnvSpec(VentureNoFrameskip-v4), EnvSpec(Venture-ram-v0), EnvSpec(Venture-ram-v4), EnvSpec(Venture-ramDeterministic-v0), EnvSpec(Venture-ramDeterministic-v4), EnvSpec(Venture-ramNoFrameskip-v0), EnvSpec(Venture-ramNoFrameskip-v4), EnvSpec(VideoPinball-v0), EnvSpec(VideoPinball-v4), EnvSpec(VideoPinballDeterministic-v0), EnvSpec(VideoPinballDeterministic-v4), EnvSpec(VideoPinballNoFrameskip-v0), EnvSpec(VideoPinballNoFrameskip-v4), EnvSpec(VideoPinball-ram-v0), EnvSpec(VideoPinball-ram-v4), EnvSpec(VideoPinball-ramDeterministic-v0), EnvSpec(VideoPinball-ramDeterministic-v4), EnvSpec(VideoPinball-ramNoFrameskip-v0), EnvSpec(VideoPinball-ramNoFrameskip-v4), EnvSpec(WizardOfWor-v0), EnvSpec(WizardOfWor-v4), EnvSpec(WizardOfWorDeterministic-v0), EnvSpec(WizardOfWorDeterministic-v4), EnvSpec(WizardOfWorNoFrameskip-v0), EnvSpec(WizardOfWorNoFrameskip-v4), EnvSpec(WizardOfWor-ram-v0), EnvSpec(WizardOfWor-ram-v4), EnvSpec(WizardOfWor-ramDeterministic-v0), EnvSpec(WizardOfWor-ramDeterministic-v4), EnvSpec(WizardOfWor-ramNoFrameskip-v0), EnvSpec(WizardOfWor-ramNoFrameskip-v4), EnvSpec(YarsRevenge-v0), EnvSpec(YarsRevenge-v4), EnvSpec(YarsRevengeDeterministic-v0), EnvSpec(YarsRevengeDeterministic-v4), EnvSpec(YarsRevengeNoFrameskip-v0), EnvSpec(YarsRevengeNoFrameskip-v4), EnvSpec(YarsRevenge-ram-v0), EnvSpec(YarsRevenge-ram-v4), EnvSpec(YarsRevenge-ramDeterministic-v0), EnvSpec(YarsRevenge-ramDeterministic-v4), EnvSpec(YarsRevenge-ramNoFrameskip-v0), EnvSpec(YarsRevenge-ramNoFrameskip-v4), EnvSpec(Zaxxon-v0), EnvSpec(Zaxxon-v4), EnvSpec(ZaxxonDeterministic-v0), EnvSpec(ZaxxonDeterministic-v4), EnvSpec(ZaxxonNoFrameskip-v0), EnvSpec(ZaxxonNoFrameskip-v4), EnvSpec(Zaxxon-ram-v0), EnvSpec(Zaxxon-ram-v4), EnvSpec(Zaxxon-ramDeterministic-v0), EnvSpec(Zaxxon-ramDeterministic-v4), EnvSpec(Zaxxon-ramNoFrameskip-v0), EnvSpec(Zaxxon-ramNoFrameskip-v4), EnvSpec(CubeCrash-v0), EnvSpec(CubeCrashSparse-v0), EnvSpec(CubeCrashScreenBecomesBlack-v0), EnvSpec(MemorizeDigits-v0)])
    

# CartPole-v1 Environment Introduction
Link: 

https://gym.openai.com/envs/CartPole-v1/

https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py

A pole is attached by an un-actuated joint to a cart, which moves along a frictionless track. The system is controlled by applying a force of +1 or -1 to the cart. The pendulum starts upright, and the goal is to prevent it from falling over. A reward of +1 is provided for every timestep that the pole remains upright. The episode ends when the pole is more than 15 degrees from vertical, or the cart moves more than 2.4 units from the center.


```python
# Simple Visualization
import gym

env = gym.make('CartPole-v1')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()
```

    [-0.01176621 -0.00560849 -0.02345143  0.03298168]
    [-0.01187838  0.18984177 -0.0227918  -0.2670072 ]
    [-0.00808154 -0.00494761 -0.02813194  0.01840078]
    [-0.00818049  0.19056626 -0.02776393 -0.28302368]
    [-0.00436917  0.38607299 -0.0334244  -0.5843323 ]
    [ 0.00335229  0.58164682 -0.04511105 -0.88735414]
    [ 0.01498523  0.38716525 -0.06285813 -0.60918671]
    [ 0.02272853  0.19297573 -0.07504186 -0.33694581]
    [ 0.02658805 -0.00100258 -0.08178078 -0.06883884]
    [ 0.026568    0.19519083 -0.08315756 -0.38616214]
    [ 0.03047181  0.39138876 -0.0908808  -0.70386222]
    [ 0.03829959  0.19763592 -0.10495804 -0.44111452]
    [ 0.04225231  0.00414369 -0.11378034 -0.18327442]
    [ 0.04233518  0.20069427 -0.11744582 -0.50957323]
    [ 0.04634907  0.00740572 -0.12763729 -0.25608745]
    [ 0.04649718 -0.18568476 -0.13275904 -0.00623135]
    [ 0.04278349  0.0110666  -0.13288366 -0.33767801]
    [ 0.04300482 -0.18193879 -0.13963722 -0.08967517]
    [ 0.03936604  0.01487976 -0.14143073 -0.42294946]
    [ 0.03966364 -0.17798501 -0.14988972 -0.177983  ]
    [ 0.03610394 -0.37067958 -0.15344938  0.06391524]
    [ 0.02869035 -0.17372861 -0.15217107 -0.27297715]
    [ 0.02521577 -0.36638884 -0.15763062 -0.03189213]
    [ 0.017888   -0.55894037 -0.15826846  0.20720256]
    [ 0.00670919 -0.75148686 -0.15412441  0.44607563]
    [-0.00832055 -0.94413089 -0.14520289  0.68648296]
    [-0.02720317 -1.13697067 -0.13147323  0.93015884]
    [-0.04994258 -0.94034277 -0.11287006  0.59922052]
    [-0.06874943 -1.13371967 -0.10088565  0.85432678]
    [-0.09142383 -1.32733259 -0.08379911  1.11365938]
    [-0.11797048 -1.52126022 -0.06152592  1.37892195]
    [-0.14839568 -1.32542636 -0.03394749  1.06764976]
    [-0.17490421 -1.52008317 -0.01259449  1.3494881 ]
    [-0.20530588 -1.32480525  0.01439527  1.05289178]
    [-0.23180198 -1.5201151   0.03545311  1.35005825]
    [-0.26220428 -1.32545603  0.06245427  1.06867417]
    [-0.2887134  -1.13121327  0.08382776  0.79622769]
    [-0.31133767 -1.32737939  0.09975231  1.11406013]
    [-0.33788526 -1.52365944  0.12203351  1.43629517]
    [-0.36835845 -1.72005626  0.15075942  1.76448841]
    [-0.40275957 -1.52692637  0.18604918  1.52223505]
    Episode finished after 41 timesteps
    [-0.04965352 -0.04881083 -0.04866795 -0.02763162]
    [-0.05062974 -0.24320229 -0.04922059  0.24930758]
    [-0.05549378 -0.43758803 -0.04423444  0.52606807]
    [-0.06424554 -0.24187247 -0.03371307  0.2197812 ]
    [-0.06908299 -0.4364967  -0.02931745  0.50164189]
    [-0.07781293 -0.63119339 -0.01928461  0.78494334]
    [-0.09043679 -0.82604513 -0.00358575  1.07149728]
    [-0.1069577  -1.02111949  0.0178442   1.36305273]
    [-0.12738009 -0.82622559  0.04510525  1.07600434]
    [-0.1439046  -0.63172764  0.06662534  0.79781059]
    [-0.15653915 -0.82769738  0.08258155  1.11068637]
    [-0.1730931  -1.02380138  0.10479528  1.42809131]
    [-0.19356913 -1.22005002  0.13335711  1.75160278]
    [-0.21797013 -1.41640991  0.16838916  2.08261832]
    Episode finished after 14 timesteps
    [ 0.01618179  0.01733171 -0.02961549  0.02855638]
    [ 0.01652842 -0.1773533  -0.02904436  0.31175015]
    [ 0.01298136 -0.37204968 -0.02280935  0.59513371]
    [ 0.00554036 -0.17661605 -0.01090668  0.29535414]
    [ 0.00200804  0.01865968 -0.0049996  -0.00074853]
    [ 0.00238123 -0.17639021 -0.00501457  0.29035278]
    [-0.00114657 -0.3714403   0.00079249  0.58144996]
    [-0.00857538 -0.56657335  0.01242149  0.87438243]
    [-0.01990684 -0.76186195  0.02990913  1.17094456]
    [-0.03514408 -0.95735979  0.05332803  1.47285214]
    [-0.05429128 -0.76292881  0.08278507  1.19729128]
    [-0.06954985 -0.95901885  0.10673089  1.51473002]
    [-0.08873023 -1.15525847  0.1370255   1.83873379]
    [-0.1118354  -0.9618906   0.17380017  1.59156028]
    [-0.13107321 -1.15859745  0.20563138  1.93301578]
    Episode finished after 15 timesteps
    [-0.01455279  0.03585994 -0.01159539 -0.01206291]
    [-0.0138356  -0.15909382 -0.01183665  0.27693909]
    [-0.01701747  0.03619498 -0.00629787 -0.01945348]
    [-0.01629357 -0.15883608 -0.00668694  0.27123576]
    [-0.01947029 -0.35386198 -0.00126222  0.56180212]
    [-0.02654753 -0.5489662   0.00997382  0.85408711]
    [-0.03752686 -0.74422266  0.02705556  1.14988949]
    [-0.05241131 -0.93968707  0.05005335  1.45093217]
    [-0.07120505 -0.74521462  0.079072    1.17429838]
    [-0.08610934 -0.55120426  0.10255796  0.90741509]
    [-0.09713343 -0.74755392  0.12070627  1.23049122]
    [-0.11208451 -0.94400392  0.14531609  1.55842365]
    [-0.13096459 -0.75088998  0.17648456  1.31437855]
    [-0.14598239 -0.55838513  0.20277213  1.08172406]
    Episode finished after 14 timesteps
    [ 0.04363911  0.01531242 -0.01272226 -0.03504645]
    [ 0.04394536 -0.1796248  -0.01342319  0.25359547]
    [ 0.04035286  0.01568622 -0.00835128 -0.04329096]
    [ 0.04066658 -0.17931499 -0.0092171   0.2467454 ]
    [ 0.03708028  0.01593738 -0.00428219 -0.0488305 ]
    [ 0.03739903  0.21112047 -0.0052588  -0.34286142]
    [ 0.04162144  0.40631684 -0.01211603 -0.637198  ]
    [ 0.04974778  0.60160564 -0.02485999 -0.93367173]
    [ 0.06177989  0.40682774 -0.04353343 -0.64890324]
    [ 0.06991645  0.60252824 -0.05651149 -0.95497065]
    [ 0.08196701  0.40821012 -0.0756109  -0.68056432]
    [ 0.09013121  0.21421528 -0.08922219 -0.41261188]
    [ 0.09441552  0.02046388 -0.09747443 -0.14933734]
    [ 0.0948248   0.21683671 -0.10046118 -0.47111048]
    [ 0.09916153  0.0232666  -0.10988338 -0.2117052 ]
    [ 0.09962686  0.21977407 -0.11411749 -0.53692942]
    [ 0.10402234  0.41629998 -0.12485608 -0.86327864]
    [ 0.11234834  0.61288039 -0.14212165 -1.19246625]
    [ 0.12460595  0.4198562  -0.16597098 -0.9474924 ]
    [ 0.13300308  0.22731088 -0.18492082 -0.711215  ]
    [ 0.13754929  0.0351655  -0.19914512 -0.48196821]
    [ 0.1382526  -0.15667081 -0.20878449 -0.25806335]
    Episode finished after 22 timesteps
    [-0.00466529 -0.0113382  -0.04716888 -0.02022975]
    [-0.00489205  0.18442735 -0.04757348 -0.32741399]
    [-0.0012035  -0.00998615 -0.05412176 -0.05010499]
    [-0.00140323  0.1858684  -0.05512386 -0.35936069]
    [ 0.00231414  0.38172886 -0.06231107 -0.66890334]
    [ 0.00994872  0.18752615 -0.07568914 -0.39647221]
    [ 0.01369924  0.38363581 -0.08361858 -0.71202585]
    [ 0.02137196  0.18976513 -0.0978591  -0.44679114]
    [ 0.02516726  0.3861254  -0.10679492 -0.76864703]
    [ 0.03288977  0.19262286 -0.12216786 -0.51138489]
    [ 0.03674223 -0.00058555 -0.13239556 -0.25956039]
    [ 0.03673051  0.19615349 -0.13758677 -0.590897  ]
    [ 0.04065358  0.0031988  -0.14940471 -0.34452313]
    [ 0.04071756 -0.18951703 -0.15629517 -0.10243147]
    [ 0.03692722  0.00745928 -0.1583438  -0.44005838]
    [ 0.03707641 -0.185109   -0.16714497 -0.20117834]
    [ 0.03337423 -0.37749519 -0.17116854  0.03446711]
    [ 0.02582432 -0.18038475 -0.17047919 -0.30695598]
    [ 0.02221663 -0.37271941 -0.17661831 -0.0725147 ]
    [ 0.01476224 -0.56492747 -0.17806861  0.15965602]
    [ 0.00346369 -0.75711251 -0.17487549  0.39129928]
    [-0.01167856 -0.94937744 -0.1670495   0.62414636]
    [-0.03066611 -1.14182187 -0.15456657  0.85991021]
    [-0.05350255 -1.33453909 -0.13736837  1.10027794]
    [-0.08019333 -1.52761249 -0.11536281  1.34690045]
    [-0.11074558 -1.72111075 -0.0884248   1.60137709]
    [-0.14516779 -1.52506006 -0.05639726  1.28248698]
    [-0.175669   -1.71942017 -0.03074752  1.55699161]
    [-2.10057399e-01 -1.91416068e+00  3.92311647e-04  1.83992596e+00]
    [-0.24834061 -2.10928696  0.03719083  2.13273069]
    [-0.29052635 -2.30475702  0.07984544  2.43666461]
    [-0.33662149 -2.50046609  0.12857874  2.75274257]
    [-0.38663081 -2.30645336  0.18363359  2.50182387]
    Episode finished after 33 timesteps
    [-0.00945519  0.0165023  -0.017421   -0.01272645]
    [-0.00912514 -0.17836554 -0.01767553  0.27440943]
    [-0.01269245 -0.37323089 -0.01218734  0.56146547]
    [-0.02015707 -0.17794005 -0.00095803  0.26496796]
    [-0.02371587  0.01719557  0.00434133 -0.02801698]
    [-0.02337196  0.21225499  0.00378099 -0.31932702]
    [-0.01912686  0.40732289 -0.00260555 -0.61081517]
    [-0.0109804   0.60248116 -0.01482186 -0.90431762]
    [ 0.00106922  0.40756306 -0.03290821 -0.61633004]
    [ 0.00922048  0.21291594 -0.04523481 -0.33419071]
    [ 0.0134788   0.40865153 -0.05191863 -0.64078826]
    [ 0.02165183  0.21429034 -0.06473439 -0.36489654]
    [ 0.02593764  0.41026968 -0.07203232 -0.67726843]
    [ 0.03414303  0.21621854 -0.08557769 -0.40810575]
    [ 0.0384674   0.02240763 -0.0937398  -0.14358241]
    [ 0.03891556 -0.17125554 -0.09661145  0.11811781]
    [ 0.03549045 -0.36487004 -0.0942491   0.37882565]
    [ 0.02819304 -0.16854482 -0.08667258  0.05797656]
    [ 0.02482215 -0.36232401 -0.08551305  0.32210442]
    [ 0.01757567 -0.55613075 -0.07907096  0.58664206]
    [ 0.00645305 -0.35999558 -0.06733812  0.2701359 ]
    [-0.00074686 -0.16398055 -0.06193541 -0.04300275]
    [-0.00402647 -0.3581622  -0.06279546  0.22951388]
    [-0.01118971 -0.55233322 -0.05820518  0.50174661]
    [-0.02223638 -0.35644119 -0.04817025  0.19130351]
    [-0.0293652  -0.55084212 -0.04434418  0.46841007]
    [-0.04038204 -0.35512267 -0.03497598  0.16208659]
    [-0.0474845  -0.54972691 -0.03173425  0.44353357]
    [-0.05847904 -0.7443858  -0.02286358  0.72604659]
    [-0.07336675 -0.93918428 -0.00834264  1.01144663]
    [-0.09215044 -1.13419392  0.01188629  1.30149821]
    [-0.11483432 -0.9392248   0.03791625  1.01255967]
    [-0.13361881 -0.74462864  0.05816745  0.73201994]
    [-0.14851138 -0.94050409  0.07280785  1.04242778]
    [-0.16732147 -0.74642065  0.0936564   0.77346051]
    [-0.18224988 -0.94269774  0.10912561  1.0940806 ]
    [-0.20110383 -0.74916919  0.13100722  0.83753381]
    [-0.21608722 -0.94581362  0.1477579   1.16837887]
    [-0.23500349 -1.1425159   0.17112548  1.50350022]
    [-0.25785381 -0.9498338   0.20119548  1.26876432]
    Episode finished after 40 timesteps
    [-0.01518646 -0.0401552  -0.01225545  0.02060312]
    [-0.01598957 -0.23509927 -0.01184339  0.30939425]
    [-0.02069155 -0.43005049 -0.0056555   0.5983187 ]
    [-0.02929256 -0.23484987  0.00631087  0.30385974]
    [-0.03398956 -0.03981842  0.01238807  0.01317378]
    [-0.03478593 -0.23511582  0.01265154  0.3097394 ]
    [-0.03948824 -0.04017639  0.01884633  0.02107311]
    [-0.04029177  0.15467028  0.01926779 -0.26560451]
    [-0.03719837  0.34951201  0.0139557  -0.55214847]
    [-0.03020813  0.54443521  0.00291273 -0.84040196]
    [-0.01931942  0.34927362 -0.01389531 -0.54680447]
    [-0.01233395  0.54458801 -0.0248314  -0.84383286]
    [-0.00144219  0.74003987 -0.04170805 -1.14421995]
    [ 0.01335861  0.93568114 -0.06459245 -1.44968525]
    [ 0.03207223  0.74140984 -0.09358616 -1.17786298]
    [ 0.04690043  0.54761957 -0.11714342 -0.9159238 ]
    [ 0.05785282  0.35425991 -0.13546189 -0.66223352]
    [ 0.06493802  0.5509806  -0.14870656 -0.99431545]
    [ 0.07595763  0.74774497 -0.16859287 -1.32976341]
    [ 0.09091253  0.94454433 -0.19518814 -1.6701089 ]
    Episode finished after 20 timesteps
    [-0.00778818  0.04436927  0.01670603 -0.03952961]
    [-0.00690079 -0.15098821  0.01591544  0.25837706]
    [-0.00992056  0.04390296  0.02108298 -0.02924372]
    [-0.0090425   0.23871632  0.0204981  -0.31520088]
    [-0.00426817  0.43354038  0.01419409 -0.60134956]
    [ 0.00440264  0.62846093  0.0021671  -0.88952801]
    [ 0.01697185  0.43330963 -0.01562346 -0.59616463]
    [ 0.02563805  0.62864671 -0.02754676 -0.89372759]
    [ 0.03821098  0.8241312  -0.04542131 -1.19494081]
    [ 0.05469361  0.62962585 -0.06932013 -0.91683297]
    [ 0.06728612  0.82561317 -0.08765678 -1.2304717 ]
    [ 0.08379839  1.02174652 -0.11226622 -1.54928028]
    [ 0.10423332  1.21802244 -0.14325182 -1.87477773]
    [ 0.12859377  1.41438846 -0.18074738 -2.20828183]
    Episode finished after 14 timesteps
    [-0.04449391  0.03153509 -0.01423203  0.0386107 ]
    [-0.04386321 -0.16337991 -0.01345981  0.32676952]
    [-0.04713081 -0.35830767 -0.00692442  0.61517761]
    [-0.05429696 -0.16308965  0.00537913  0.32032185]
    [-0.05755876  0.03195528  0.01178557  0.02934014]
    [-0.05691965  0.22690625  0.01237237 -0.25960114]
    [-0.05238153  0.03160988  0.00718035  0.03695838]
    [-0.05174933 -0.1636143   0.00791952  0.33189811]
    [-0.05502161 -0.35884807  0.01455748  0.6270679 ]
    [-0.06219857 -0.55417016  0.02709884  0.92429973]
    [-0.07328198 -0.35942453  0.04558483  0.64025462]
    [-0.08047047 -0.55515137  0.05838992  0.94693719]
    [-0.0915735  -0.75100896  0.07732867  1.25737979]
    [-0.10659368 -0.55695718  0.10247626  0.98988394]
    [-0.11773282 -0.36334507  0.12227394  0.73106467]
    [-0.12499972 -0.17010603  0.13689523  0.47922926]
    [-0.12840184  0.02284472  0.14647982  0.23263248]
    [-0.12794495  0.2156031   0.15113247 -0.01049748]
    [-0.12363288  0.01867318  0.15092252  0.32579423]
    [-0.12325942  0.21136026  0.1574384   0.08425205]
    [-0.11903222  0.40391617  0.15912345 -0.15491365]
    [-0.11095389  0.2069161   0.15602517  0.18343839]
    [-0.10681557  0.3995014   0.15969394 -0.05624497]
    [-0.09882554  0.20249294  0.15856904  0.28225834]
    [-0.09477568  0.00550647  0.16421421  0.62045521]
    [-0.09466555 -0.19148184  0.17662331  0.96002486]
    [-0.09849519  0.00088287  0.19582381  0.72762453]
    Episode finished after 27 timesteps
    [ 0.04758363 -0.04435379  0.01839138  0.03869072]
    [ 0.04669656 -0.23973458  0.0191652   0.33711911]
    [ 0.04190186 -0.04489053  0.02590758  0.05054093]
    [ 0.04100405  0.14985054  0.0269184  -0.23385667]
    [ 0.04400106 -0.04564548  0.02224127  0.06719417]
    [ 0.04308815  0.14915065  0.02358515 -0.21838937]
    [ 0.04607117  0.34392766  0.01921736 -0.50354022]
    [ 0.05294972  0.1485402   0.00914656 -0.2048636 ]
    [ 0.05592052 -0.04671135  0.00504928  0.09069052]
    [ 0.0549863  -0.24190531  0.0068631   0.38496221]
    [ 0.05014819 -0.43712402  0.01456234  0.67980112]
    [ 0.04140571 -0.63244519  0.02815836  0.97703298]
    [ 0.02875681 -0.43771193  0.04769902  0.69332636]
    [ 0.02000257 -0.243283    0.06156555  0.41603286]
    [ 0.01513691 -0.04908516  0.06988621  0.14337682]
    [ 0.01415521 -0.24513477  0.07275374  0.45726321]
    [ 0.00925251 -0.44120581  0.08189901  0.77196248]
    [ 4.28394348e-04 -2.47300554e-01  9.73382563e-02  5.06130911e-01]
    [-0.00451762 -0.0536753   0.10746087  0.24564013]
    [-0.00559112  0.13976084  0.11237368 -0.01130763]
    [-0.00279591  0.33310684  0.11214752 -0.26652903]
    [ 0.00386623  0.52646444  0.10681694 -0.52184114]
    [ 0.01439552  0.33001391  0.09638012 -0.19750036]
    [0.0209958  0.13365499 0.09243011 0.12396299]
    [ 0.0236689   0.32733954  0.09490937 -0.13818792]
    [ 0.03021569  0.52098303  0.09214562 -0.39948442]
    [ 0.04063535  0.32468298  0.08415593 -0.07923104]
    [0.04712901 0.12846176 0.08257131 0.2387718 ]
    [ 0.04969824  0.322313    0.08734674 -0.02676596]
    [ 0.0561445   0.51608079  0.08681142 -0.29066231]
    [0.06646612 0.31983517 0.08099818 0.02808812]
    [0.07286282 0.1236507  0.08155994 0.34518746]
    [0.07533584 0.31752346 0.08846369 0.07929707]
    [0.08168631 0.12125206 0.09004963 0.39852735]
    [ 0.08411135 -0.07502429  0.09802018  0.7181878 ]
    [ 0.08261086 -0.27135618  0.11238393  1.04004381]
    [ 0.07718374 -0.46777723  0.13318481  1.3657881 ]
    [ 0.06782819 -0.27455049  0.16050057  1.11755548]
    [ 0.06233718 -0.47137238  0.18285168  1.45597865]
    Episode finished after 39 timesteps
    [-0.01884099 -0.02336752 -0.03780833  0.0214601 ]
    [-0.01930834 -0.21792744 -0.03737913  0.30197841]
    [-0.02366689 -0.41249726 -0.03133956  0.58264237]
    [-0.03191684 -0.60716644 -0.01968672  0.86529043]
    [-0.04406017 -0.80201498 -0.00238091  1.15171909]
    [-0.06010047 -0.99710579  0.02065347  1.44365448]
    [-0.08004258 -1.19247577  0.04952656  1.74271864]
    [-0.1038921  -0.99795114  0.08438094  1.46584434]
    [-0.12385112 -0.80395775  0.11369782  1.20066815]
    [-0.13993028 -0.61047503  0.13771119  0.94567314]
    [-0.15213978 -0.41744958  0.15662465  0.69923531]
    [-0.16048877 -0.22480586  0.17060936  0.45966646]
    [-0.16498489 -0.42187673  0.17980268  0.80089716]
    [-0.17342242 -0.2296162   0.19582063  0.56973314]
    [-0.17801474 -0.03770137  0.20721529  0.34456664]
    Episode finished after 15 timesteps
    [ 0.02204083 -0.03663476  0.03369547  0.00769079]
    [ 0.02130813  0.15798816  0.03384929 -0.27417328]
    [ 0.0244679   0.3526112   0.02836582 -0.55599082]
    [ 0.03152012  0.54732366  0.01724601 -0.83960358]
    [ 4.24665942e-02  3.51970533e-01  4.53934190e-04 -5.41547396e-01]
    [ 0.049506    0.5470861  -0.01037701 -0.83408726]
    [ 0.06044773  0.35210745 -0.02705876 -0.54468582]
    [ 0.06748988  0.54759898 -0.03795248 -0.84577007]
    [ 0.07844186  0.74321761 -0.05486788 -1.15014207]
    [ 0.09330621  0.93901101 -0.07787072 -1.45951327]
    [ 0.11208643  0.7449256  -0.10706098 -1.19213825]
    [ 0.12698494  0.94125906 -0.13090375 -1.5163681 ]
    [ 0.14581012  0.74794128 -0.16123111 -1.26724825]
    [ 0.16076895  0.55520368 -0.18657608 -1.02908829]
    [ 0.17187302  0.36298813 -0.20715784 -0.80030444]
    Episode finished after 15 timesteps
    [ 0.04255835  0.04771563  0.00061311 -0.00385201]
    [ 0.04351266  0.24282878  0.00053607 -0.29634143]
    [ 0.04836924  0.43794309 -0.00539075 -0.58885524]
    [ 0.0571281   0.63314011 -0.01716786 -0.88323139]
    [ 0.0697909   0.43825546 -0.03483249 -0.59599459]
    [ 0.07855601  0.63384713 -0.04675238 -0.89944281]
    [ 0.09123295  0.43938889 -0.06474124 -0.62181437]
    [ 0.10002073  0.63535231 -0.07717752 -0.93416433]
    [ 0.11272778  0.83142578 -0.09586081 -1.25006673]
    [ 0.12935629  1.02763667 -0.12086214 -1.57117174]
    [ 0.14990902  1.22397592 -0.15228558 -1.89897921]
    [ 0.17438854  1.42038384 -0.19026516 -2.23478065]
    Episode finished after 12 timesteps
    [-0.00925319 -0.00019736  0.00036561 -0.03600497]
    [-0.00925714  0.19491935 -0.00035449 -0.32857252]
    [-0.00535875  0.39004634 -0.00692594 -0.62136722]
    [ 0.00244218  0.19502179 -0.01935329 -0.33087362]
    [ 0.00634261  0.39041381 -0.02597076 -0.62959627]
    [ 0.01415089  0.19566372 -0.03856269 -0.34520419]
    [ 0.01806416  0.3913124  -0.04546677 -0.64979366]
    [ 0.02589041  0.19685229 -0.05846264 -0.37176755]
    [ 0.02982746  0.00260751 -0.06589799 -0.0980764 ]
    [ 0.02987961  0.19860899 -0.06785952 -0.41080049]
    [ 0.03385179  0.39462406 -0.07607553 -0.72408176]
    [ 0.04174427  0.20063205 -0.09055717 -0.45628003]
    [ 0.04575691  0.0068993  -0.09968277 -0.19345906]
    [ 0.0458949   0.20329544 -0.10355195 -0.51584906]
    [ 0.0499608   0.00977244 -0.11386893 -0.25750944]
    [ 0.05015625 -0.18355527 -0.11901912 -0.00280104]
    [ 0.04648515  0.01305469 -0.11907514 -0.3305387 ]
    [ 0.04674624  0.20965259 -0.12568591 -0.65827278]
    [ 0.05093929  0.01648335 -0.13885137 -0.40765897]
    [ 0.05126896 -0.17642481 -0.14700455 -0.16177291]
    [ 0.04774046  0.02046233 -0.15024001 -0.4969821 ]
    [ 0.04814971 -0.1722574  -0.16017965 -0.25516353]
    [ 0.04470456  0.02474584 -0.16528292 -0.59377722]
    [ 0.04519948 -0.167724   -0.17715846 -0.3573792 ]
    [ 0.041845   -0.3599432  -0.18430605 -0.12537577]
    [ 0.03464614 -0.16272496 -0.18681356 -0.47007263]
    [ 0.03139164 -0.3547849  -0.19621502 -0.24159946]
    [ 0.02429594 -0.54664204 -0.201047   -0.01665369]
    [ 0.0133631  -0.34928976 -0.20138008 -0.36542994]
    [ 0.0063773  -0.15196091 -0.20868868 -0.71424802]
    Episode finished after 30 timesteps
    [ 0.03199939 -0.00578519 -0.03360995 -0.00507967]
    [ 0.03188369  0.18980225 -0.03371155 -0.30817461]
    [ 0.03567973  0.38538793 -0.03987504 -0.61129575]
    [ 0.04338749  0.58104385 -0.05210096 -0.9162665 ]
    [ 0.05500837  0.77683015 -0.07042629 -1.22485819]
    [ 0.07054497  0.58268223 -0.09492345 -0.95504643]
    [ 0.08219862  0.38895645 -0.11402438 -0.69363156]
    [ 0.08997775  0.1955854  -0.12789701 -0.4389091 ]
    [ 0.09388945  0.00248363 -0.13667519 -0.18912154]
    [ 0.09393913 -0.1904452  -0.14045762  0.05751546]
    [ 0.09013022 -0.38330306 -0.13930731  0.30279445]
    [ 0.08246416 -0.18649906 -0.13325142 -0.03037572]
    [ 0.07873418 -0.3794834  -0.13385894  0.21747455]
    [ 0.07114451 -0.57246312 -0.12950945  0.4651175 ]
    [ 0.05969525 -0.37577182 -0.1202071   0.13458195]
    [ 0.05217981 -0.5689852  -0.11751546  0.38705479]
    [ 0.04080011 -0.37240824 -0.10977436  0.05975296]
    [ 0.03335194 -0.56579903 -0.1085793   0.31588418]
    [ 0.02203596 -0.75922036 -0.10226162  0.57244797]
    [ 0.00685156 -0.95277098 -0.09081266  0.83124465]
    [-0.01220386 -1.14654222 -0.07418777  1.09404158]
    [-0.03513471 -1.34061265 -0.05230694  1.3625553 ]
    [-0.06194696 -1.53504162 -0.02505583  1.63842865]
    [-0.09264779 -1.72986105  0.00771274  1.92320042]
    [-0.12724501 -1.92506493  0.04617675  2.21826506]
    [-0.16574631 -1.73041303  0.09054205  1.94016958]
    [-0.20035457 -1.92637712  0.12934545  2.25949468]
    [-0.23888212 -2.12245231  0.17453534  2.58907222]
    Episode finished after 28 timesteps
    [-0.03761038 -0.02399463  0.03509318  0.04827758]
    [-0.03809028 -0.21960175  0.03605874  0.35182289]
    [-0.04248231 -0.02501064  0.04309519  0.07072494]
    [-0.04298252 -0.22072309  0.04450969  0.3766871 ]
    [-0.04739699 -0.02626064  0.05204343  0.09836385]
    [-0.0479222   0.16807829  0.05401071 -0.17745599]
    [-0.04456063  0.36238738  0.05046159 -0.45262317]
    [-0.03731289  0.1665895   0.04140913 -0.14447079]
    [-0.0339811   0.36109471  0.03851971 -0.4238077 ]
    [-0.0267592   0.55565042  0.03004356 -0.70410278]
    [-0.01564619  0.75034343  0.0159615  -0.98717904]
    [-6.39324089e-04  9.45248053e-01 -3.78207861e-03 -1.27480625e+00]
    [ 0.01826564  0.75017455 -0.0292782  -0.98331001]
    [ 0.03326913  0.55545685 -0.0489444  -0.6999652 ]
    [ 0.04437826  0.75122194 -0.06294371 -1.00764509]
    [ 0.0594027   0.55699423 -0.08309661 -0.73537371]
    [ 0.07054259  0.36311247 -0.09780408 -0.46995686]
    [ 0.07780484  0.16949829 -0.10720322 -0.20963209]
    [ 0.0811948  -0.02394051 -0.11139586  0.04740296]
    [ 0.08071599 -0.21730346 -0.1104478   0.30296698]
    [ 0.07636992 -0.41069223 -0.10438846  0.55887694]
    [ 0.06815608 -0.21427185 -0.09321093  0.23521569]
    [ 0.06387064 -0.01795032 -0.08850661 -0.08535261]
    [ 0.06351164 -0.21169944 -0.09021366  0.17814654]
    [ 0.05927765 -0.40542234 -0.08665073  0.44106238]
    [ 0.0511692  -0.59921803 -0.07782949  0.70522183]
    [ 0.03918484 -0.40310886 -0.06372505  0.38908979]
    [ 0.03112266 -0.20714303 -0.05594325  0.0770152 ]
    [ 0.0269798  -0.01126557 -0.05440295 -0.23278007]
    [ 0.02675449 -0.20556968 -0.05905855  0.04225831]
    [ 0.0226431  -0.3997972  -0.05821338  0.31573854]
    [ 0.01464715 -0.20389645 -0.05189861  0.0052801 ]
    [ 0.01056922 -0.39823717 -0.05179301  0.28114733]
    [ 0.00260448 -0.20241616 -0.04617006 -0.02741065]
    [-0.00144384 -0.00666354 -0.04671828 -0.33429584]
    [-0.00157711  0.18909111 -0.05340419 -0.64133761]
    [ 0.00220471 -0.00524731 -0.06623095 -0.36593895]
    [ 0.00209976 -0.19936861 -0.07354973 -0.09485306]
    [-0.00188761 -0.00327378 -0.07544679 -0.40980422]
    [-0.00195309  0.19283222 -0.08364287 -0.72528671]
    [ 0.00190356 -0.00103962 -0.09814861 -0.46005797]
    [ 0.00188277  0.1953227  -0.10734977 -0.78199329]
    [ 0.00578922  0.39174349 -0.12298963 -1.10642869]
    [ 0.01362409  0.58824864 -0.1451182  -1.43502777]
    [ 0.02538906  0.39518369 -0.17381876 -1.1909895 ]
    [ 0.03329274  0.59207831 -0.19763855 -1.53272685]
    Episode finished after 46 timesteps
    [-0.03350298 -0.04800904 -0.02933193  0.01116048]
    [-0.03446316  0.14752102 -0.02910872 -0.2906308 ]
    [-0.03151274 -0.04717404 -0.03492134 -0.00726869]
    [-0.03245622  0.14843088 -0.03506671 -0.31076197]
    [-0.0294876  -0.04617438 -0.04128195 -0.02934104]
    [-0.03041109  0.14951452 -0.04186877 -0.33475776]
    [-0.0274208  -0.04498731 -0.04856393 -0.05556651]
    [-0.02832055  0.15079612 -0.04967526 -0.36316759]
    [-0.02530463 -0.04358591 -0.05693861 -0.08655275]
    [-0.02617634  0.15230403 -0.05866967 -0.39664238]
    [-0.02313026 -0.04193858 -0.06660251 -0.12301877]
    [-0.02396903  0.15407122 -0.06906289 -0.43594827]
    [-0.02088761  0.35009938 -0.07778185 -0.7495779 ]
    [-0.01388562  0.54620312 -0.09277341 -1.06568894]
    [-0.00296156  0.35242309 -0.11408719 -0.80350517]
    [ 0.0040869   0.15903484 -0.1301573  -0.54877749]
    [ 0.0072676  -0.03404163 -0.14113284 -0.2997708 ]
    [ 0.00658677 -0.22689941 -0.14712826 -0.05471587]
    [ 0.00204878 -0.03000779 -0.14822258 -0.38996234]
    [ 0.00144862  0.1668728  -0.15602183 -0.72546311]
    [ 0.00478608 -0.02578711 -0.17053109 -0.48566808]
    [ 0.00427034 -0.21814423 -0.18024445 -0.25121117]
    [-9.25488812e-05 -2.09676371e-02 -1.85268672e-01 -5.94890029e-01]
    [-0.0005119  -0.21307955 -0.19716647 -0.36581156]
    [-0.00477349 -0.40493344 -0.2044827  -0.14119841]
    [-0.01287216 -0.20755942 -0.20730667 -0.49079118]
    Episode finished after 26 timesteps
    [ 0.03640471 -0.0480616  -0.03182063  0.04573193]
    [ 0.03544347 -0.24271316 -0.03090599  0.32820776]
    [ 0.03058921 -0.4373818  -0.02434184  0.61098636]
    [ 0.02184157 -0.24192823 -0.01212211  0.31073706]
    [ 0.01700301 -0.43687539 -0.00590737  0.59957251]
    [ 0.0082655  -0.6319142   0.00608408  0.89038886]
    [-0.00437278 -0.43687532  0.02389186  0.59962467]
    [-0.01311029 -0.63232324  0.03588435  0.89973642]
    [-0.02575675 -0.43770548  0.05387908  0.61854544]
    [-0.03451086 -0.63353698  0.06624999  0.92769922]
    [-0.0471816  -0.82948786  0.08480397  1.24044399]
    [-0.06377136 -1.0255901   0.10961285  1.55844274]
    [-0.08428316 -0.83193795  0.14078171  1.30186951]
    [-0.10092192 -0.63885459  0.1668191   1.05636308]
    [-0.11369901 -0.44628865  0.18794636  0.82034164]
    [-0.12262479 -0.64341679  0.20435319  1.1657582 ]
    Episode finished after 16 timesteps
    [-0.01018458 -0.02517386  0.01243874  0.04729808]
    [-0.01068806  0.16976754  0.0133847  -0.2414345 ]
    [-0.00729271 -0.02554302  0.00855601  0.05544009]
    [-0.00780357  0.16945521  0.00966481 -0.23453112]
    [-0.00441446 -0.02580348  0.00497419  0.06118466]
    [-0.00493053  0.1692468   0.00619788 -0.22992474]
    [-0.0015456  -0.02596317  0.00159939  0.06470676]
    [-0.00206486 -0.22110802  0.00289353  0.35789387]
    [-0.00648702 -0.41627098  0.0100514   0.65148779]
    [-0.01481244 -0.22129045  0.02308116  0.36198684]
    [-0.01923825 -0.02650404  0.0303209   0.0766703 ]
    [-0.01976833 -0.22204725  0.0318543   0.37876327]
    [-0.02420928 -0.02739182  0.03942957  0.09629183]
    [-0.02475711 -0.22305606  0.0413554   0.40114936]
    [-0.02921823 -0.41873947  0.04937839  0.70657852]
    [-0.03759302 -0.61450948  0.06350996  1.01438697]
    [-0.04988321 -0.42028944  0.0837977   0.74230363]
    [-0.058289   -0.616462    0.09864377  1.06013763]
    [-0.07061824 -0.42277506  0.11984653  0.79997384]
    [-0.07907374 -0.229483    0.135846    0.54726607]
    [-0.0836634  -0.03650481  0.14679132  0.30028161]
    [-0.0843935   0.15625318  0.15279696  0.05725598]
    [-0.08126844 -0.04069183  0.15394208  0.39397937]
    [-0.08208227  0.15194889  0.16182166  0.15351588]
    [-0.07904329  0.34442849  0.16489198 -0.08406332]
    [-0.07215472  0.53685006  0.16321071 -0.32052183]
    [-0.06141772  0.33982568  0.15680028  0.01885846]
    [-0.05462121  0.14284319  0.15717745  0.35661793]
    [-0.05176435  0.33542209  0.16430981  0.11733059]
    [-0.0450559   0.52785525  0.16665642 -0.11934145]
    [-0.0344988   0.72024604  0.16426959 -0.35515876]
    [-0.02009388  0.52321604  0.15716641 -0.01551403]
    [-0.00962956  0.71577579  0.15685613 -0.2547767 ]
    [0.00468596 0.51880261 0.1517606  0.08298262]
    [ 0.01506201  0.71146019  0.15342025 -0.15823572]
    [0.02929121 0.51451261 0.15025554 0.1786445 ]
    [ 0.03958147  0.7072007   0.15382843 -0.06312198]
    [0.05372548 0.51024619 0.15256599 0.27386865]
    [0.0639304  0.70289946 0.15804336 0.03292602]
    [ 0.07798839  0.89544358  0.15870188 -0.20601911]
    [ 0.09589726  1.08798222  0.1545815  -0.44473496]
    [ 0.11765691  0.89104979  0.1456868  -0.10759246]
    [ 0.1354779   1.0838162   0.14353495 -0.35099838]
    [ 0.15715423  0.8869758   0.13651498 -0.01671956]
    [ 0.17489374  1.07990275  0.13618059 -0.26340672]
    [0.1964918  0.88312639 0.13091246 0.06893857]
    [ 0.21415433  1.07615217  0.13229123 -0.17974415]
    [ 0.23567737  1.26915737  0.12869634 -0.42794204]
    [ 0.26106052  1.46224416  0.1201375  -0.67744463]
    [ 0.2903054   1.65551023  0.10658861 -0.93001866]
    [ 0.32341561  1.4591236   0.08798824 -0.60583278]
    [ 0.35259808  1.65291215  0.07587158 -0.86955592]
    [ 0.38565632  1.4568446   0.05848046 -0.55401584]
    [ 0.41479321  1.65109871  0.04740015 -0.82771544]
    [ 0.44781519  1.45536182  0.03084584 -0.52050944]
    [ 0.47692242  1.65003628  0.02043565 -0.80331498]
    [ 0.50992315  1.45464017  0.00436935 -0.50427435]
    [ 0.53901595  1.64970027 -0.00571614 -0.79557713]
    [ 0.57200996  1.45465723 -0.02162768 -0.50469788]
    [ 0.6011031   1.6500772  -0.03172164 -0.80411732]
    [ 0.63410465  1.45540419 -0.04780398 -0.52157932]
    [ 0.66321273  1.65116529 -0.05823557 -0.82893453]
    [ 0.69623604  1.84703297 -0.07481426 -1.13934958]
    [ 0.7331767   1.65296464 -0.09760125 -0.87103625]
    [ 0.76623599  1.84926894 -0.11502198 -1.19274055]
    [ 0.80322137  2.04567737 -0.13887679 -1.51914842]
    [ 0.84413491  2.2421783  -0.16925976 -1.85176064]
    [ 0.88897848  2.04927467 -0.20629497 -1.61606527]
    Episode finished after 68 timesteps
    

## CartPole-v1 environment details

(From https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py)


- Description:

    A pole is attached by an un-actuated joint to a cart, which moves along
    a frictionless track. The pendulum starts upright, and the goal is to
    prevent it from falling over by increasing and reducing the cart's
    velocity.
    

- Observation:

        Type: Box(4)
        Num   Observation               Min             Max
        0     Cart Position             -4.8            4.8
        1     Cart Velocity             -Inf            Inf
        2     Pole Angle                -24 deg         24 deg
        3     Pole Velocity At Tip      -Inf            Inf

- Actions:

        Type: Discrete(2)
        Num   Action
        0     Push cart to the left
        1     Push cart to the right

    Note: The amount the velocity that is reduced or increased is not
    fixed; it depends on the angle the pole is pointing. This is because
    the center of gravity of the pole increases the amount of energy needed
    to move the cart underneath it


- Reward:

    Reward is 1 for every step taken, including the termination step


- Starting State:

    All observations are assigned a uniform random value in [-0.05,0.05]


- **Episode Termination**:

    - Pole Angle is more than **12 degrees (around 0.209 rad)**.

    - Cart Position is more than **2.4** (center of the cart reaches the edge of the display). 
    
    - Episode length is greater than 200.


- Solved Requirements:

    Considered solved when the average reward is greater than or equal to 195.0 over 100 consecutive trials.


### Physical Parameters Initialization

    self.gravity = 9.8  
    self.masscart = 1.0  
    self.masspole = 0.1  
    self.total_mass = (self.masspole + self.masscart)  
    self.length = 0.5  # actually half the pole's length  
    self.polemass_length = (self.masspole * self.length)    
    self.force_mag = 10.0  # The force appilied to the cart in an action(0->-10, 1->10)  
    self.tau = 0.02  # seconds between state updates  
    self.kinematics_integrator = 'euler'  

    #### Angle at which to fail the episode
    self.theta_threshold_radians = 12 * 2 * math.pi / 360       # 12 degree = 0.209 rad  
    self.x_threshold = 2.4  

    #### Angle limit set to 2 * theta_threshold_radians so failing observation is still within bounds.
    high = np.array([self.x_threshold * 2,
                     np.finfo(np.float32).max,
                     self.theta_threshold_radians * 2,
                     np.finfo(np.float32).max],
                    dtype=np.float32)  

    ( [4.8, inf, 24degree, inf])    

    self.action_space = spaces.Discrete(2)  
    self.observation_space = spaces.Box(-high, high, dtype=np.float32)  
    self.seed()  
    self.viewer = None  
    self.state = None  
    self.steps_beyond_done = None  


```python
# Check
print(env.action_space)
print(env.observation_space)
print(env.observation_space.high)
print(env.observation_space.low)
```

    Discrete(2)
    Box(4,)
    [4.8000002e+00 3.4028235e+38 4.1887903e-01 3.4028235e+38]
    [-4.8000002e+00 -3.4028235e+38 -4.1887903e-01 -3.4028235e+38]
    

### Motion Model


---

$$
\ddot{\theta} = \frac{(M+m)g sin\theta - cos\theta[F+ml\dot{\theta}^2sin\theta]}{\frac{4}{3}(M+m)l - m l cos^2\theta}
$$
$$
\ddot{p} = \frac{F+ml[\dot{\theta}^2 sin\theta - \ddot{\theta} cos\theta]}{M+m}
$$

Where $\theta$ and $\dot{\theta}$ is the angular position and velocity of pendulum, $p$ and $\dot{p}$ is the position and velocity of cart, $M$ is the mass of cart, $m$ is the mass of pendulum, $g$ is gravitational acceleration, $F$ is the force applied to the cart, $l$ is the length from the center of mass to the pivot.

---


    x, x_dot, theta, theta_dot = self.state  
    force = self.force_mag if action == 1 else -self.force_mag  
    costheta = math.cos(theta)  
    sintheta = math.sin(theta)  

#For the interested reader:  
#https://coneural.org/florian/papers/05_cart_pole.pdf  

    temp = (force + self.polemass_length * theta_dot ** 2 * sintheta) / self.total_mass
    thetaacc = (self.gravity * sintheta - costheta * temp) / (self.length * (4.0 / 3.0 - self.masspole * costheta ** 2 / self.total_mass))
    xacc = temp - self.polemass_length * thetaacc * costheta / self.total_mass

    if self.kinematics_integrator == 'euler': # By default   
        x = x + self.tau * x_dot  
        x_dot = x_dot + self.tau * xacc  
        theta = theta + self.tau * theta_dot  
        theta_dot = theta_dot + self.tau * thetaacc  
    else:  # semi-implicit euler  
        x_dot = x_dot + self.tau * xacc  
        x = x + self.tau * x_dot  
        theta_dot = theta_dot + self.tau * thetaacc  
        theta = theta + self.tau * theta_dot  
  
    self.state = (x, x_dot, theta, theta_dot)  

### Episode Termination
---
    done = bool(
                x < -self.x_threshold
                or x > self.x_threshold
                or theta < -self.theta_threshold_radians
                or theta > self.theta_threshold_radians
            )

### Reward
--- 
    if not done:  # Not reach Termination
        reward = 1.0
    elif self.steps_beyond_done is None:
        # Pole just fell!
        self.steps_beyond_done = 0
        reward = 1.0
    else:
        if self.steps_beyond_done == 0:
            logger.warn(
                "You are calling 'step()' even though this "
                "environment has already returned done = True. You "
                "should always call 'reset()' once you receive 'done = "
                "True' -- any further steps are undefined behavior."
            )
        self.steps_beyond_done += 1
        reward = 0.0

### Reset 
--- 
    def reset(self):
            self.state = self.np_random.uniform(low=-0.05, high=0.05, size=(4,))
            self.steps_beyond_done = None
            return np.array(self.state)


```python

```