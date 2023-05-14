python
# 僵尸王类
class ZombieKing(Zombie): 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("zombie_king.png")
        self.rect = self.image.get_rect()
        self.hp = 10
        self.speed = 1
    
    def move(self):
        super().move() 
        # 每10帧召唤一只普通僵尸
        if pygame.time.get_ticks() % 10 == 0: 
            zombies.add(Zombie())
            
# 僵尸球类          
class ZombieBall(Zombie):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("zombie_ball.png")
        self.rect = self.image.get_rect()
        self.hp = 3
        self.speed = 3
        
    def move(self):
        super().move()
        # 每3秒改变移动方向
        if pygame.time.get_ticks() % 3000 == 0:
            self.speed = -self.speed  
            
# 在游戏循环中根据时间新增僵尸         
zombie_timer = pygame.time.Clock()
zombie_timer.tick(1)  

if total_time > 20 and total_time % 10 == 0:
    zombies.add(ZombieKing())
if total_time > 10 and total_time % 5 == 0: 
    zombies.add(ZombieBall()) 
else:
    zombies.add(Zombie()) 
    
# 活动:僵尸关卡,全部清除僵尸才算通关
if level.is_zombie_level: 
    if len(zombies) == 0:
        show_message("关卡通关!")
        now_time = get_game_time()  # 获取当前游戏时间
        if now_time < best_time:  # 如果更快通关,更新最佳记录
            best_time = now_time
            save_player_data()  # 保存玩家数据
        go_next_level()  # 进入下一关

# 活动:加倍收获阳光活动  
double_sunshine_duration = 120  # 活动持续时间
double_sunshine_start = 0
if event.is_double_sunshine and now - double_sunshine_start < double_sunshine_duration:
    sunshine_value = sunshine_value * 2  # 阳光产出加倍
else:
    double_sunshine_start = now  # 更新活动启动时间

# 活动:僵尸关卡限时通关 
if level.is_zombie_level:
    finish_time = get_level_time() + 180  # 3分钟内通关
    if now_time >= finish_time:
        show_message("限时未通关, GAME OVER!")
        # 游戏结束,所有植物清除
        for plant in plants: 
            plant.kill() 
else:
    finish_time = 0  # 活动时间重置        

# 活动:随机奖励,概率获得额外阳光或金币  
if random.random() < 0.2:  # 20%概率触发奖励
    gift = random.choice(["sunshine", "money"])
    if gift == "sunshine":
        sunshine_value += 50  # 额外50点阳光
    else:
        coins += 50  # 额外50金币
    show_message(f"恭喜你,获得{gift}奖励!")
