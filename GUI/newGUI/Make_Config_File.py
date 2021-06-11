def makeConfig():
    f = open('office_portal.txt', "w+")
    f.writelines([targetipWidth + '\n', targetipHeight + '\n', str(ledStrip) + '\n', str(ledTexture) + '\n', str(noRing) + '\n', str(autoStart) + '\n', streamBitrate + '\n', portSender + '\n', portReceiver,])
    f.close()
    print('file made')
