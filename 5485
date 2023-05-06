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
