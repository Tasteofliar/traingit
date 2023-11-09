import maya.cmds as cmds

def createSphere(name,num):
    counter = 0
    amp = 2
    for i in range(num):
        for j in range(num):
            objName = '{}{}_geo'.format(name, '%04d' % (counter+1))
            obj = cmds.polySphere(name=objName)[0]

            cmds.setAttr('{}.tx'.format(obj), (i*amp))
            cmds.setAttr('{}.tz'.format(obj), (j*amp))

            counter+=1
            print(objName)