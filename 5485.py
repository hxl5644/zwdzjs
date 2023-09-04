python
import pygame
from pygame.locals import *
import random

# 常量定义
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 游戏类
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
        pygame.display.set_caption('植物大战僵尸')  

        # 加载资源
        self.load_resources()

        # 创建精灵组
        self.plants = pygame.sprite.Group()
        self.zombies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        # 游戏参数
        self.sunlight = 100
        self.selected_plant = None
        self.wave = 1

    def load_resources(self):
        # 加载植物资源
        self.plant_sprites = {
            'peashooter': pygame.image.load('peashooter.png')
        }
        
        # 加载僵尸资源
        self.zombie_sprites = {
            'normal': pygame.image.load('zombie.png')
        }
        
        # 加载背景资源
        self.bg_image = pygame.image.load('bg.jpg')

    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            # 限制帧率
            clock.tick(30)
            
            # 事件循环
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    
                if event.type == MOUSEBUTTONDOWN:
                    # 种植植物
                    if self.selected_plant:
                        plant = Plant(self.selected_plant, mouse_x, mouse_y)  
                        self.plants.add(plant)
                        self.sunlight -= plant.sunlight_cost
            
            # 更新游戏
            self.update()
            
            # 绘制游戏
            self.draw()
            
            pygame.display.update()

        pygame.quit()

    def update(self):
        # 生成僵尸
        if random.random() < 0.1:
            zombie = Zombie(self.zombie_sprites['normal'], 800, random.randint(0, 600))
            self.zombies.add(zombie)
            
        # 碰撞检测
        hits = pygame.sprite.groupcollide(self.zombies, self.bullets, False, True)
        for zombie in hits:
            zombie.hit()
            
        # 更新植物、僵尸、子弹
        self.plants.update()
        self.zombies.update()
        self.bullets.update()

    def draw(self):
        # 绘制背景
        self.screen.blit(self.bg_image, (0,0))
        
        # 绘制阳光
        draw_text(self.screen, 'Sunlight: %d' % self.sunlight, 24, (10, 10))
        
        # 绘制植物和僵尸
        self.plants.draw(self.screen)
        self.zombies.draw(self.screen)
        
if __name__ == '__main__':
    game = Game()
    game.run()
    python
# 导入模块
import pygame
from pygame.locals import *

# 游戏类
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('植物大战僵尸')

        # 加载资源
        self.load_resources()

        # 创建精灵组
        self.plants = pygame.sprite.Group() 
        self.zombies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        # 游戏参数
        self.sunlight = 50
        self.selected_plant = None

    def load_resources(self):
        # 加载植物和僵尸资源
        pass

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(30)
            
            # 处理事件
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            # 更新游戏
            self.update()

            # 绘制游戏
            self.draw()

            pygame.display.update()

        pygame.quit()

    def update(self):
        # 生成僵尸
        pass

        # 子弹碰撞检测
        pass

        # 更新植物、僵尸、子弹
        self.plants.update()
        self.zombies.update() 
        self.bullets.update()

    def draw(self):
        self.screen.fill((255,255,255))
        self.plants.draw(self.screen)
        self.zombies.draw(self.screen)
        self.bullets.draw(self.screen)
        
if __name__ == '__main__':
    game = Game() 
    game.run()

后续可以继续扩展:1. 实现阳光系统,种植植物需要花费阳光2. 加载并绘制背景图片和地图3. 用户交互,选择植物,鼠标拖放种植4. 更多植物和僵尸类型,不同能力5. 实现波次系统,控制僵尸生成6. 增加音效和UI界面7. 保存和读取游戏进度以及更多丰富的游戏玩法内容。 （已编辑） 
  晚上 10:35
继续
应用  晚上 10:35
好的,让我继续扩展植物大战僵尸的代码:

python
import pygame
from pygame.locals import *

# 常量定义
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 游戏类
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('植物大战僵尸')
        
        # 加载资源
        self.load_resources()
        
        # 创建精灵组
        self.plants = pygame.sprite.Group()
        self.zombies = pygame.sprite.Group()
        
        # 游戏参数
        self.sunlight = 100
        self.selected_plant = None
        
    def load_resources(self):
        # 加载植物图像
        self.plant_sprites = {
            'peashooter': pygame.image.load('peashooter.png') 
        }
        
        # 加载僵尸图像
        self.zombie_sprites = {
            'normal': pygame.image.load('zombie.png')
        }
        
        # 加载背景图像
        self.bg_image = pygame.image.load('bg.jpg')
        
    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            # 限制帧率
            clock.tick(30)
            
            # 事件循环
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    
                if event.type == MOUSEBUTTONDOWN:
                    # 处理点击事件,种植植物
                    if self.selected_plant:
                        plant = Plant(self.selected_plant, mouse_x, mouse_y)
                        self.plants.add(plant)
                        self.sunlight -= plant.sunlight_cost
                        
            # 更新游戏
            self.update()
            
            # 绘制游戏
            self.draw()
            
            pygame.display.update()
            
        pygame.quit()
        
    def update(self):
        # 生成僵尸逻辑
        pass
        
        # 碰撞检测逻辑
        pass
        
        # 更新植物和僵尸组
        self.plants.update()
        self.zombies.update()
        
    def draw(self):
        # 绘制背景
        self.screen.blit(self.bg_image, (0,0))
        
        # 绘制阳光
        draw_text(self.screen, 'Sunlight: %d' % self.sunlight, 24, (10, 10))
        
        # 绘制植物和僵尸
        self.plants.draw(self.screen)
        self.zombies.draw(self.screen)
        
if __name__ == '__main__':
    game = Game()
    game.run()
