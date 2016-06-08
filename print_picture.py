import gym
from PIL import Image
train=file("train.txt","w")
val=file("val.txt","w")
env = gym.make('Pong-v0')
env.reset()

for i in range(2500):
    picture=env.render(mode="rgb_array")
    env.step(env.action_space.sample()) # take a random action
    img = Image.fromarray(picture, 'RGB')
    img.save('train/Pong_'+str(i+1)+'.jpg')
    train.write('Pong_'+str(i+1)+'.jpg'+' 0\n')
train.close()

for i in range(2500,3000):
    picture=env.render(mode="rgb_array")
    env.step(env.action_space.sample()) # take a random action
    img = Image.fromarray(picture, 'RGB')
    img.save('val/Pong_'+str(i+1)+'.jpg')
    val.write('Pong_'+str(i+1)+'.jpg'+' 0\n')
val.close()

    

	

    



