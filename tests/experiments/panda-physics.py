from panda3d.core import Vec3, ClockObject
from panda3d.bullet import BulletWorld
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape
from direct.showbase import ShowBase
base = ShowBase.ShowBase()

base.cam.setPos(10, -30, 20)
base.cam.lookAt(0, 0, 5)

# World
world = BulletWorld()
world.setGravity(Vec3(0, 0, -9.81))

# Plane
shape = BulletPlaneShape(Vec3(0, 0, 1), 1)
node = BulletRigidBodyNode('Ground')
node.addShape(shape)
np = base.render.attachNewNode(node)
np.setPos(0, 0, -2)
world.attachRigidBody(node)

# Boxes
model = base.loader.loadModel('models/box.egg')
model.setPos(-0.5, -0.5, -0.5)
model.flattenLight()
shape = BulletBoxShape(Vec3(0.5, 0.5, 0.5))
for i in range(10):
    node = BulletRigidBodyNode('Box')
    node.setMass(1.0)
    node.addShape(shape)
    np = base.render.attachNewNode(node)
    np.setPos(0, 0, 2 + i * 2)
    world.attachRigidBody(node)
    model.copyTo(np)

globalClock = ClockObject.getGlobalClock()

# Update
def update(task):
    dt = globalClock.getDt()
    world.doPhysics(dt)
    return task.cont


base.taskMgr.add(update, 'update')
base.run()