 #!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.78.01), October 16, 2013, at 11:01
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

# TEMPLATE FILE FOR EYETRACKING EXPERIMENTS ############################################

#from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
import numpy,shutil, os, time
from random import random,randint,shuffle
from psychopy import visual, core, gui, misc, sound, data, event
from numpy import pi
import random, copy
from random import shuffle

# Import IOHUB libraries
from psychopy.iohub import (ioHubExperimentRuntime, module_directory, getCurrentDateTimeString, EyeTrackerConstants)

class ExperimentRuntime(ioHubExperimentRuntime): 
    def run(self,*args):
        # PUT ANY FUNCTIONS IN HERE
        
        # Let's make some short-cuts to the devices we will be using in this experiment
        display=self.hub.devices.display
        kb=self.hub.devices.kb
        mouse=self.hub.devices.mouse      
        mouse.setSystemCursorVisibility(False)
        tracker=self.hub.devices.tracker  
        tracker.setRecordingState(False)      
        
        # Information about screen
        info=display.getRuntimeInfo()
        physDim = display.getPhysicalDimensions()
        eyeDist = display.getDefaultEyeDistance()
        #params['viewing_distance']=eyeDist/10.0 #in cm
        #params['screen_width']=physDim['width']/10.0
        #params['refresh_rate']=float(info['retrace_rate'])
        
        # Create a psychopy window, full screen resolution, full screen mode...
        res=display.getPixelResolution()
        win=visual.Window(res,monitor='benq',
                                    units='deg',
                                    fullscr=True,
                                    allowGUI=False,
                                    screen= display.getIndex()
                                    )
                                
        # Setup eye tracker and calibrate 
        win.winHandle.minimize()           
        tracker.runSetupProcedure()       
        win.winHandle.maximize()
        win.winHandle.activate()        
        win.flip() 
            
        # Send experiment info to iohub
        self.hub.sendMessageEvent(text="IO_HUB EXPERIMENT_INFO START")
        self.hub.sendMessageEvent(text="contSens_eyeTrack_mark2.py") # Name of file
        self.hub.sendMessageEvent(text="ioHub Experiment started {0}".format(getCurrentDateTimeString()))
        self.hub.sendMessageEvent(text="Experiment ID: {0}, Session ID: {1}".format(self.hub.experimentID,self.hub.experimentSessionID))
        self.hub.sendMessageEvent(text="Stimulus Screen ID: {0}, Size (pixels): {1}, CoordType: {2}".format(display.getIndex(),display.getPixelResolution(),display.getCoordinateType()))
        self.hub.sendMessageEvent(text="Calculated Pixels Per Degree: {0} x, {1} y".format(*display.getPixelsPerDegree()))
        self.hub.sendMessageEvent(text="Resolution: {0}, {1}".format(*display.getPixelResolution()))
        self.hub.sendMessageEvent(text="Width, Height, EyeDist: %i %i %i" %(physDim['width'],physDim['height'],eyeDist))
        self.hub.sendMessageEvent(text="Refresh rate: %i" %(info['retrace_rate']))
        self.hub.sendMessageEvent(text="IO_HUB EXPERIMENT_INFO END") 
        
        flip_time=win.flip()
        self.hub.sendMessageEvent(text="EXPERIMENT_START",sec_time=flip_time)
            
        tracker.setRecordingState(True) 
        mouse.setSystemCursorVisibility(False)
                
        ## EXPERIMENT GOES HERE:
        ###############################################################
        ###############################################################
        #Start of the trials for IoHub
        
        #This section creates the trials
        
        expName = 'CIT_Experiment'
        thisPath = os.path.split(__file__)[0]
        os.chdir(thisPath)
        
        expInfo = {}
        
        expInfo['date'] = data.getDateStr()  # add a simple timestamp
        
        #IMPORTANT NEED TO CHANGE INFO FOR EACH PARTICIPANT
        expInfo['participant'] = 'p18 f 22 '
        
        
        filename = 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])
        ##create psychopy experiment handler
        thisExp = data.ExperimentHandler(version='',
            extraInfo=expInfo, 
            savePickle=True, saveWideText=True,
            dataFileName=filename)
            
            
        print('Created EXPinfo')
        #print(trial)
        
        #This section creates the trials
        
        Matrix = [[0 for x in xrange(6)] for x in xrange(6)]
        
        
        Matrix[0][0] = 1
        Matrix[0][1] = 2
        Matrix[0][2] = 5
        Matrix[0][3] = 6
        Matrix[0][4] = 7
        Matrix[0][5] = 8
        
        Matrix[1][0] = 1
        Matrix[1][1] = 3
        Matrix[1][2] = 9
        Matrix[1][3] = 11
        Matrix[1][4] = 7
        Matrix[1][5] = 12
        
        Matrix[2][0] = 1
        Matrix[2][1] = 4
        Matrix[2][2] = 9
        Matrix[2][3] = 12
        Matrix[2][4] = 6
        Matrix[2][5] = 10
        
        Matrix[3][0] = 2
        Matrix[3][1] = 3
        Matrix[3][2] = 8
        Matrix[3][3] = 10
        Matrix[3][4] = 5
        Matrix[3][5] = 9
        
        Matrix[4][0] = 2
        Matrix[4][1] = 4
        Matrix[4][2] = 8
        Matrix[4][3] = 11
        Matrix[4][4] = 7
        Matrix[4][5] = 12
        
        Matrix[5][0] = 3
        Matrix[5][1] = 4
        Matrix[5][2] = 5
        Matrix[5][3] = 6
        Matrix[5][4] = 11
        Matrix[5][5] = 10
        
        
        #Thise section Loads into trial handler
        print('Created trials')
        trialsList = []
        
        
        for trial in range(6):
            thisTrial = {}
            order = range(6)
            random.shuffle(order)
            for i in range(6):
                
                id = Matrix[trial][order[i]]
                
                if(id ==1):
                    text = 'Berlin'
                elif(id == 2):
                    text = 'Paris'
                elif(id == 3):
                    text = 'Brussels'
                elif(id == 4):
                    text = 'Madrid'
                elif(id == 5):
                    text = 'Vienna'
                elif(id == 6):
                    text = 'Athens'
                elif(id == 7):
                    text = 'London'
                elif(id == 8):
                    text = 'Stockholm'
                elif(id == 9):
                    text = 'Istanbul'
                elif(id == 10):
                    text = 'Warsaw'
                elif(id == 11):
                    text = 'Budapest'
                elif(id == 12):
                    text = 'Helsinki'
                else:
                    text = id
                
                thisTrial[i] = text
            trialsList.append(thisTrial)
            
        print('SavedTrials')
        #This has been appended as of 19 July 15:12PM. this is so that things are actually in line
        positions = [
        (-10, 10),
        (10, 10),
        (-10, -10),
        (10, -10),
        (0, -10),
        (1, 10),
        ]
        
        #This section creates the objects we need for the experiment
        
        Target = visual.TextStim(win, text = "text default")
        
        fixation = visual.GratingStim(win, tex=None, mask='raisedCos', size=20, units='pix')
        
        responseClock = core.Clock()
        
        #Message to IOHUB at start of the experiment
        #self.hub.sendMessageEvent(text="EXPERIMENT_START",sec_time=flip_time)
        
        
        #Messagesfor the study#
        message1 = visual.TextStim(win, text = "You have been randomly selected for questioning by the people involved. In order to see if you have knowledge regarding the money laundering incident, an on screen test will be adminstered. Press Spacebar when ready")
        message1.draw()
        win.update()
        response = event.waitKeys(keyList = ['space',], timeStamped = True)#this will wait for a button press confirmation from p's to continue
        
        message2 = visual.TextStim(win, text = "You will be presented with four blocks of test. In each block, there are two conditions. In the deception condition, you should try and conceal the knowledge you have. In the Truthful condition, you should tell the truth .Press Spacebar when ready")
        message2.draw()
        win.update()
        response = event.waitKeys(keyList = ['space',], timeStamped = True)#this will wait for a button press confirmation from p's to continue
        
        message3 = visual.TextStim(win, text = "In order to respond to the question presented, press Q to indicate Yes and P to indicate No. When you are ready to answer the question, press the spacebar")
        message3.draw()
        win.update()
        response = event.waitKeys(keyList = ['space',], timeStamped = True)#this will wait for a button press confirmation from p's to continue
        
        message4 = visual.TextStim(win, text = "Are any of these cities involved in the incident? Respond only when you are confident in your answer")
        message4.draw()
        win.update()
        response = event.waitKeys(keyList = ['space',], timeStamped = True)#this will wait for a button press confirmation from p's to continue
        
        message5 = visual.TextStim(win, text = "Deception")
        message5.draw()
        win.update()
        core.wait(2)
        
        
        trials = data.TrialHandler(trialList=trialsList, nReps=1,
        method='random', 
        extraInfo=expInfo, name='trials')
        thisExp.addLoop(trials)
        
        AorB = 1
        
        trialCounter = 0
        
        for trial in trials:
            trialCounter = trialCounter+1
            fixation.draw()
            win.flip()
            core.wait(1)
            flip_time=win.flip()
            #self.hub.sendMessageEvent(text="RUN_START" ,sec_time=flip_time)
            #self.hub.sendMessageEvent(text="City_Deception",sec_time=flip_time)
            for i in range(6):
                # Prepare stimulus
                #fixation.draw()
                # Show it 
                Target.pos = positions[i]
                Target.text = trial[i]
                Target.draw()
            
            presTime = win.flip() #this corresponds to the presentation of the images
            responseClock.reset()
            boop = 0
            while boop == 0:
                resp = event.waitKeys()
                allKeys =('p''q')
                keyPressTime = core.getTime() # record time as soon as key press is sensed
                if resp == ["escape"]:
                    core.quit()
                if resp == ["p"]:
                    boop = 1
                if resp == ["q"]:
                    boop = 1
            
            trials.addData('respDetect.keys', resp)
            trials.addData('respDetect.rt', responseClock.getTime())
            trials.addData('Trial Type', 'Deception')
             
            RT = keyPressTime - presTime;
            
            #self.hub.sendMessageEvent(text='%.6f' %(RT),sec_time=flip_time)#This works and is recoridng the RT to 6 the 6DP
            self.hub.sendMessageEvent(text='%.6f' %(RT) + ' responseTime ' + '%.6f' %(presTime)+ ' presTime ' + '%i' %(trialCounter) + ' DeceptiveCityTrial ')
            
            
            win.flip()
            
            
            
            thisExp.nextEntry()
        
        #######################Loop for the truthful condition#############
        message6 = visual.TextStim(win, text = "Truthful")
        message6.draw()
        win.update()
        core.wait(2)
        
        #fixation.draw()
        #win.flip()
        #core.wait(2)
        
        trials = data.TrialHandler(trialList=trialsList, nReps=1,
        method='random', 
        extraInfo=expInfo, name='trials')
        thisExp.addLoop(trials)
        
        AorB = 1
        
        for trial in trials:
            trialCounter = trialCounter+1
            fixation.draw()
            win.flip()
            core.wait(1)
            for i in range(6):
                # Prepare stimulus
                #fixation.draw()
                # Show it 
                Target.pos = positions[i]
                Target.text = trial[i]
                Target.draw()
            
            presTime = win.flip() #this corresponds to the presentation of the images
            responseClock.reset()
            boop = 0
            while boop == 0:
                resp = event.waitKeys()
                allKeys =('p''q')
                keyPressTime = core.getTime() # record time as soon as key press is sensed
                if resp == ["escape"]:
                    core.quit()
                if resp == ["p"]:
                    boop = 1
                if resp == ["q"]:
                    boop = 1
            
            trials.addData('respDetect.keys', resp)
            trials.addData('respDetect.rt', responseClock.getTime())
            trials.addData('Trial Type', 'Truthful')
             
            RT = keyPressTime - presTime;
            
            #self.hub.sendMessageEvent(text='%.6f' %(RT),sec_time=flip_time)#This works and is recoridng the RT to 6 the 6DP
            self.hub.sendMessageEvent(text='%.6f' %(RT) + ' responseTime ' + '%.6f' %(presTime)+ ' presTime ' + '%i' %(trialCounter) + ' TruthfulCityTrial ')
            
            
            win.flip()
            
            
            
            thisExp.nextEntry()
            
        
        ########Month Block############
        
        message7 = visual.TextStim(win, text = "Are any of these months involved in the incident? Respond only when you are confident in your answer.")
        message7.draw()
        win.update()
        response = event.waitKeys(keyList = ['space',], timeStamped = True)#this will wait for a button press confirmation from p's to continue
        
        #This section creates the trials
        
        Matrix = [[0 for x in xrange(6)] for x in xrange(6)]
        
        
        Matrix[0][0] = 1
        Matrix[0][1] = 2
        Matrix[0][2] = 5
        Matrix[0][3] = 6
        Matrix[0][4] = 7
        Matrix[0][5] = 8
        
        Matrix[1][0] = 1
        Matrix[1][1] = 3
        Matrix[1][2] = 9
        Matrix[1][3] = 11
        Matrix[1][4] = 7
        Matrix[1][5] = 12
        
        Matrix[2][0] = 1
        Matrix[2][1] = 4
        Matrix[2][2] = 9
        Matrix[2][3] = 12
        Matrix[2][4] = 6
        Matrix[2][5] = 10
        
        Matrix[3][0] = 2
        Matrix[3][1] = 3
        Matrix[3][2] = 8
        Matrix[3][3] = 10
        Matrix[3][4] = 5
        Matrix[3][5] = 9
        
        Matrix[4][0] = 2
        Matrix[4][1] = 4
        Matrix[4][2] = 8
        Matrix[4][3] = 11
        Matrix[4][4] = 7
        Matrix[4][5] = 12
        
        Matrix[5][0] = 3
        Matrix[5][1] = 4
        Matrix[5][2] = 5
        Matrix[5][3] = 6
        Matrix[5][4] = 11
        Matrix[5][5] = 10
        
        #Thise section Loads into trial handler
        print('Created trials')
        trialsList = []
        
        for trial in range(6):
            thisTrial = {}
            order = range(6)
            random.shuffle(order)
            for i in range(6):
                id = Matrix[trial][order[i]]
        
                if(id ==1):
                    text = 'January'
                elif(id == 2):
                    text = 'Febuary'
                elif(id == 3):
                    text = 'March'
                elif(id == 4):
                    text = 'April'
                elif(id == 5):
                    text = 'May'
                elif(id == 6):
                    text = 'June'
                elif(id == 7):
                    text = 'July'
                elif(id == 8):
                    text = 'August'
                elif(id == 9):
                    text = 'September'
                elif(id == 10):
                    text = 'October'
                elif(id == 11):
                    text = 'November'
                elif(id == 12):
                    text = 'December'
                else:
                    text = id
        
                thisTrial[i] = text
            trialsList.append(thisTrial)
        
        print('SavedTrials')
        
        #This section creates the objects we need for the experiment
        #This is a deceptive block
        trials = data.TrialHandler(trialList=trialsList, nReps=1,
        method='random', 
        extraInfo=expInfo, name='trials')
        thisExp.addLoop(trials)
        
        message8 = visual.TextStim(win, text = "Truthful")
        message8.draw()
        win.update()
        core.wait(2)
        AorB = 1
        
        for trial in trials:
            trialCounter = trialCounter+1
            fixation.draw()
            win.flip()
            core.wait(1)
            for i in range(6):
                # Prepare stimulus
                #fixation.draw()
                # Show it 
                Target.pos = positions[i]
                Target.text = trial[i]
                Target.draw()
            
            presTime = win.flip() #this corresponds to the presentation of the images
            responseClock.reset()
            boop = 0
            while boop == 0:
                resp = event.waitKeys()
                allKeys =('p''q')
                keyPressTime = core.getTime() # record time as soon as key press is sensed
                if resp == ["escape"]:
                    core.quit()
                if resp == ["p"]:
                    boop = 1
                if resp == ["q"]:
                    boop = 1
            
            trials.addData('respDetect.keys', resp)
            trials.addData('respDetect.rt', responseClock.getTime())
            trials.addData('Trial Type', 'Truthful')
             
            RT = keyPressTime - presTime;
            
            #self.hub.sendMessageEvent(text='%.6f' %(RT),sec_time=flip_time)#This works and is recoridng the RT to 6 the 6DP
            self.hub.sendMessageEvent(text='%.6f' %(RT) + ' responseTime ' + '%.6f' %(presTime)+ ' presTime ' + '%i' %(trialCounter) + ' TruthfulMonthTrial ')
            
            
            
            
            thisExp.nextEntry()
            ############Deception#########
        message5 = visual.TextStim(win, text = "Deception")
        message5.draw()
        win.update()
        core.wait(2)
        
        
        trials = data.TrialHandler(trialList=trialsList, nReps=1,
        method='random', 
        extraInfo=expInfo, name='trials')
        thisExp.addLoop(trials)
        
        AorB = 1
        
        
        
        for trial in trials:
            trialCounter = trialCounter+1
            fixation.draw()
            win.flip()
            core.wait(1)
            flip_time=win.flip()
            #self.hub.sendMessageEvent(text="RUN_START" ,sec_time=flip_time)
            #self.hub.sendMessageEvent(text="City_Deception",sec_time=flip_time)
            for i in range(6):
                # Prepare stimulus
                #fixation.draw()
                # Show it 
                Target.pos = positions[i]
                Target.text = trial[i]
                Target.draw()
            
            presTime = win.flip() #this corresponds to the presentation of the images
            responseClock.reset()
            boop = 0
            while boop == 0:
                resp = event.waitKeys()
                allKeys =('p''q')
                keyPressTime = core.getTime() # record time as soon as key press is sensed
                if resp == ["escape"]:
                    core.quit()
                if resp == ["p"]:
                    boop = 1
                if resp == ["q"]:
                    boop = 1
            
            trials.addData('respDetect.keys', resp)
            trials.addData('respDetect.rt', responseClock.getTime())
            trials.addData('Trial Type', 'Deception')
             
            RT = keyPressTime - presTime;
            
            #self.hub.sendMessageEvent(text='%.6f' %(RT),sec_time=flip_time)#This works and is recoridng the RT to 6 the 6DP
            self.hub.sendMessageEvent(text='%.6f' %(RT) + ' responseTime ' + '%.6f' %(presTime)+ ' presTime ' + '%i' %(trialCounter) + ' DeceptiveMonthTrial ')
            
            
            win.flip()
            
            
            
            thisExp.nextEntry()
           
        ######Amount block#######
        message10 = visual.TextStim(win, text = "Are any of these amounts involved in the incident? Respond only when you are confident in your answer")
        message10.draw()
        win.update()
        response = event.waitKeys(keyList = ['space',], timeStamped = True)#this will wait for a button press confirmation from p's to continue
        
        #This section creates the trials
        
        Matrix = [[0 for x in xrange(6)] for x in xrange(6)]
        
        
        Matrix[0][0] = 1
        Matrix[0][1] = 2
        Matrix[0][2] = 5
        Matrix[0][3] = 6
        Matrix[0][4] = 7
        Matrix[0][5] = 8
        
        Matrix[1][0] = 1
        Matrix[1][1] = 3
        Matrix[1][2] = 9
        Matrix[1][3] = 11
        Matrix[1][4] = 7
        Matrix[1][5] = 12
        
        Matrix[2][0] = 1
        Matrix[2][1] = 4
        Matrix[2][2] = 9
        Matrix[2][3] = 12
        Matrix[2][4] = 6
        Matrix[2][5] = 10
        
        Matrix[3][0] = 2
        Matrix[3][1] = 3
        Matrix[3][2] = 8
        Matrix[3][3] = 10
        Matrix[3][4] = 5
        Matrix[3][5] = 9
        
        Matrix[4][0] = 2
        Matrix[4][1] = 4
        Matrix[4][2] = 8
        Matrix[4][3] = 11
        Matrix[4][4] = 7
        Matrix[4][5] = 12
        
        Matrix[5][0] = 3
        Matrix[5][1] = 4
        Matrix[5][2] = 5
        Matrix[5][3] = 6
        Matrix[5][4] = 11
        Matrix[5][5] = 10
        
        #Thise section Loads into trial handler
        print('Created trials')
        trialsList = []
        
        
        for trial in range(6):
            thisTrial = {}
            order = range(6)
            random.shuffle(order)
            for i in range(6):
                id = Matrix[trial][order[i]]
        
                if(id ==1):
                    text = '10,000'
                elif(id == 2):
                    text = '50,000'
                elif(id == 3):
                    text = '100,000'
                elif(id == 4):
                    text = '200,000'
                elif(id == 5):
                    text = '45,000'
                elif(id == 6):
                    text = '75,000'
                elif(id == 7):
                    text = '250,000'
                elif(id == 8):
                    text = '300,000'
                elif(id == 9):
                    text = '400,000'
                elif(id == 10):
                    text = '450,000'
                elif(id == 11):
                    text = '500,000'
                elif(id == 12):
                    text = '550,000'
                else:
                    text = id
                
                thisTrial[i] = text
            trialsList.append(thisTrial)
                
            print('SavedTrials')
        
        
        message5 = visual.TextStim(win, text = "Deception")
        message5.draw()
        win.update()
        core.wait(2)
        
        
        trials = data.TrialHandler(trialList=trialsList, nReps=1,
        method='random', 
        extraInfo=expInfo, name='trials')
        thisExp.addLoop(trials)
        
        AorB = 1
        
        
        
        for trial in trials:
            trialCounter = trialCounter+1
            fixation.draw()
            win.flip()
            core.wait(1)
            flip_time=win.flip()
            #self.hub.sendMessageEvent(text="RUN_START" ,sec_time=flip_time)
            #self.hub.sendMessageEvent(text="City_Deception",sec_time=flip_time)
            for i in range(6):
                # Prepare stimulus
                #fixation.draw()
                # Show it 
                Target.pos = positions[i]
                Target.text = trial[i]
                Target.draw()
            
            presTime = win.flip() #this corresponds to the presentation of the images
            responseClock.reset()
            boop = 0
            while boop == 0:
                resp = event.waitKeys()
                allKeys =('p''q')
                keyPressTime = core.getTime() # record time as soon as key press is sensed
                if resp == ["escape"]:
                    core.quit()
                if resp == ["p"]:
                    boop = 1
                if resp == ["q"]:
                    boop = 1
            
            trials.addData('respDetect.keys', resp)
            trials.addData('respDetect.rt', responseClock.getTime())
            trials.addData('Trial Type', 'Deception')
             
            RT = keyPressTime - presTime;
            
            #self.hub.sendMessageEvent(text='%.6f' %(RT),sec_time=flip_time)#This works and is recoridng the RT to 6 the 6DP
            self.hub.sendMessageEvent(text='%.6f' %(RT) + ' responseTime ' + '%.6f' %(presTime)+ ' presTime ' + '%i' %(trialCounter) + ' DeceptiveAmountTrial ')
            
            
            win.flip()
            
            
            
            thisExp.nextEntry()
            
        ############Truthful block#########
        message5 = visual.TextStim(win, text = "Truthful")
        message5.draw()
        win.update()
        core.wait(2)
        
        
        trials = data.TrialHandler(trialList=trialsList, nReps=1,
        method='random', 
        extraInfo=expInfo, name='trials')
        thisExp.addLoop(trials)
        
        AorB = 1
        
        
        
        for trial in trials:
            trialCounter = trialCounter+1
            fixation.draw()
            win.flip()
            core.wait(1)
            flip_time=win.flip()
            #self.hub.sendMessageEvent(text="RUN_START" ,sec_time=flip_time)
            #self.hub.sendMessageEvent(text="City_Deception",sec_time=flip_time)
            for i in range(6):
                # Prepare stimulus
                #fixation.draw()
                # Show it 
                Target.pos = positions[i]
                Target.text = trial[i]
                Target.draw()
            
            presTime = win.flip() #this corresponds to the presentation of the images
            responseClock.reset()
            boop = 0
            while boop == 0:
                resp = event.waitKeys()
                allKeys =('p''q')
                keyPressTime = core.getTime() # record time as soon as key press is sensed
                if resp == ["escape"]:
                    core.quit()
                if resp == ["p"]:
                    boop = 1
                if resp == ["q"]:
                    boop = 1
            
            trials.addData('respDetect.keys', resp)
            trials.addData('respDetect.rt', responseClock.getTime())
            trials.addData('Trial Type', 'Truthful')
             
            RT = keyPressTime - presTime;
            
            #self.hub.sendMessageEvent(text='%.6f' %(RT),sec_time=flip_time)#This works and is recoridng the RT to 6 the 6DP
            self.hub.sendMessageEvent(text='%.6f' %(RT) + ' responseTime ' + '%.6f' %(presTime)+ ' presTime ' + '%i' %(trialCounter) + ' TruthfulAmountTrial ')
            
            
            win.flip()
            
            
            
            thisExp.nextEntry()
            
            
           
        ##Face's Block#############
        message13 = visual.TextStim(win, text = "Are any of these people involved in the incident? Respond only when you are confident in your answer")
        message13.draw()
        win.update()
        response = event.waitKeys(keyList = ['space',], timeStamped = True)#this will wait for a button press confirmation from p's to continue
        
        #This section creates the trials
        
        Matrix = [[0 for x in xrange(6)] for x in xrange(6)]
        
        Matrix[0][0] = 1
        Matrix[0][1] = 2
        Matrix[0][2] = 5
        Matrix[0][3] = 6
        Matrix[0][4] = 7
        Matrix[0][5] = 8
        
        Matrix[1][0] = 1
        Matrix[1][1] = 3
        Matrix[1][2] = 9
        Matrix[1][3] = 11
        Matrix[1][4] = 7
        Matrix[1][5] = 12
        
        Matrix[2][0] = 1
        Matrix[2][1] = 4
        Matrix[2][2] = 9
        Matrix[2][3] = 12
        Matrix[2][4] = 6
        Matrix[2][5] = 10
        
        Matrix[3][0] = 2
        Matrix[3][1] = 3
        Matrix[3][2] = 8
        Matrix[3][3] = 10
        Matrix[3][4] = 5
        Matrix[3][5] = 9
        
        Matrix[4][0] = 2
        Matrix[4][1] = 4
        Matrix[4][2] = 8
        Matrix[4][3] = 11
        Matrix[4][4] = 7
        Matrix[4][5] = 12
        
        Matrix[5][0] = 3
        Matrix[5][1] = 4
        Matrix[5][2] = 5
        Matrix[5][3] = 6
        Matrix[5][4] = 11
        Matrix[5][5] = 10
        
        #Thise section Loads into trial handler
        print('Created trials')
        trialsList = []
        
        for trial in range(6):
            thisTrial = {}
            order = range(6)
            random.shuffle(order)
            for i in range(6):
                
                id = Matrix[trial][order[i]]
                
                if(id ==1):
                    image = 'Face.1.jpg'
                elif(id == 2):
                    image = 'Face.2.jpg'
                elif(id == 3):
                    image = 'Face.3.jpg'
                elif(id == 4):
                    image = 'Face.4.jpg'
                elif(id == 5):
                    image = 'Face.5.jpg'
                elif(id == 6):
                    image = 'Face.6.jpg'
                elif(id == 7):
                    image = 'Face.7.jpg'
                elif(id == 8):
                    image = 'Face.8.jpg'
                elif(id == 9):
                    image = 'Face.9.jpg'
                elif(id == 10):
                    image = 'Face.10.jpg'
                elif(id == 11):
                    image = 'Face.11.jpg'
                elif(id == 12):
                    image = 'Face.12.jpg'
                else:
                    image = id
        
                thisTrial[i] = image
            trialsList.append(thisTrial)
            
        print('SavedTrials')
        
        #These positions have to be altered in order to accomodate for the images
        #This has been appended as of 19 July 15:12PM. this is so that things are actually in line
        positions = [
         (-10, 10),
         (10, 10),
         (-10, -10),
         (10, -10),
         (0, -10),
         (1, 10),
         ]
        
        #This section creates the objects we need for the experiment
        
        trials = data.TrialHandler(trialList=trialsList, nReps=1,
            method='random', 
            extraInfo=expInfo, name='trials')
        thisExp.addLoop(trials)
        
        #Create the message stimuli

        
        #img1 = visual.ImageStim(win, size=[50, 50])
        fixation = visual.GratingStim(win, tex=None, mask='raisedCos', size=20, units='pix')
        
        Target = visual.ImageStim(win, size=[5, 5])
        
        responseClock = core.Clock()
        
        message5 = visual.TextStim(win, text = "Truthful")
        message5.draw()
        win.update()
        core.wait(2)
        
        
        trials = data.TrialHandler(trialList=trialsList, nReps=1,
        method='random', 
        extraInfo=expInfo, name='trials')
        thisExp.addLoop(trials)
        
        AorB = 1
        
        
        
        for trial in trials:
            trialCounter = trialCounter+1
            fixation.draw()
            win.flip()
            core.wait(1)
            flip_time=win.flip()
            #self.hub.sendMessageEvent(text="RUN_START" ,sec_time=flip_time)
            #self.hub.sendMessageEvent(text="City_Deception",sec_time=flip_time)
            for i in range(6):
                # Prepare stimulus
                #fixation.draw()
                # Show it 
                Target.pos = positions[i]
                Target.image = trial[i]
                Target.draw()
            
            presTime = win.flip() #this corresponds to the presentation of the images
            responseClock.reset()
            boop = 0
            while boop == 0:
                resp = event.waitKeys()
                allKeys =('p''q')
                keyPressTime = core.getTime() # record time as soon as key press is sensed
                if resp == ["escape"]:
                    core.quit()
                if resp == ["p"]:
                    boop = 1
                if resp == ["q"]:
                    boop = 1
            
            trials.addData('respDetect.keys', resp)
            trials.addData('respDetect.rt', responseClock.getTime())
            trials.addData('Trial Type', 'Truthful')
             
            RT = keyPressTime - presTime;
            
            #self.hub.sendMessageEvent(text='%.6f' %(RT),sec_time=flip_time)#This works and is recoridng the RT to 6 the 6DP
            self.hub.sendMessageEvent(text='%.6f' %(RT) + ' responseTime ' + '%.6f' %(presTime)+ ' presTime ' + '%i' %(trialCounter) + ' TruthfulFaceTrial ')
            
            
            win.flip()
            
            
            
            thisExp.nextEntry()
        
        
        #This is the deceptive block of the faces
        message5 = visual.TextStim(win, text = "Deception")
        message5.draw()
        win.update()
        core.wait(2)
        
        
        trials = data.TrialHandler(trialList=trialsList, nReps=1,
        method='random', 
        extraInfo=expInfo, name='trials')
        thisExp.addLoop(trials)
        
        AorB = 1
        
        
        
        for trial in trials:
            trialCounter = trialCounter+1
            fixation.draw()
            win.flip()
            core.wait(1)
            flip_time=win.flip()
            #self.hub.sendMessageEvent(text="RUN_START" ,sec_time=flip_time)
            #self.hub.sendMessageEvent(text="City_Deception",sec_time=flip_time)
            for i in range(6):
                # Prepare stimulus
                #fixation.draw()
                # Show it 
                Target.pos = positions[i]
                Target.image = trial[i]
                Target.draw()
            
            presTime = win.flip() #this corresponds to the presentation of the images
            responseClock.reset()
            boop = 0
            while boop == 0:
                resp = event.waitKeys()
                allKeys =('p''q')
                keyPressTime = core.getTime() # record time as soon as key press is sensed
                if resp == ["escape"]:
                    core.quit()
                if resp == ["p"]:
                    boop = 1
                if resp == ["q"]:
                    boop = 1
            
            trials.addData('respDetect.keys', resp)
            trials.addData('respDetect.rt', responseClock.getTime())
            trials.addData('Trial Type', 'Deception')
             
            RT = keyPressTime - presTime;
            
            #self.hub.sendMessageEvent(text='%.6f' %(RT),sec_time=flip_time)#This works and is recoridng the RT to 6 the 6DP
            self.hub.sendMessageEvent(text='%.6f' %(RT) + ' responseTime ' + '%.6f' %(presTime)+ ' presTime ' + '%i' %(trialCounter) + ' DeceptiveFaceTrial ')
            
            
            win.flip()
            
            
            
            thisExp.nextEntry()
        
        #End of experiment message
        message16 = visual.TextStim(win, text = "That is the end of the experiment! Thank you for taking part. Press the spacebar to finish")
        message16.draw()
        win.update()
        response = event.waitKeys(keyList = ['space',], timeStamped = True)#this will wait for a button press confirmation from p's to continue
           
        ## EXAMPLES OF CODED MSGS TO IOHUB
        ## RUN START
#            flip_time=win.flip()
#            self.hub.sendMessageEvent(text="RUN_START " + str(reps+1),sec_time=flip_time)
#                
#            ## TRIAL INFO
#            self.hub.sendMessageEvent(text='%i  %.4f %i	 %.6f %i %i' %(reps+1,params['SpatFreq'],targetOri, thisIncrement, thisResp, frames2Wait),sec_time=flip_time)
#    
#            ## RUN END    
#            flip_time=win.flip()
#            self.hub.sendMessageEvent(text="RUN_END " + str(reps+1),sec_time=flip_time) 
          
        ## AFTER EXPERIMENT
        # End and close everything             
        mouse.setSystemCursorVisibility(True)
        self.hub.clearEvents('all')
        tracker.setRecordingState(False)    
        tracker.setConnectionState(False)
        flip_time=win.flip()
        self.hub.sendMessageEvent(text="EXPERIMENT_END",sec_time=flip_time)
        core.wait(3)
        win.close()
        self.hub.quit()  
        
        # Save hdf5 file as something other than events.hdf5
        params = {'sub':'cs',
            'runnum':1}
        
        initDir = 'C:\\bwebb\\Python\\scholes\\'
        #initDir = 'E:\CIT experiment\Code for experiment\CIT Final\Eye tracking Code\Eye tracking attempts\attempt at simple CIT'
        #endDir = 'C:\\bwebb\\Python\\scholes\\hdf5_files\\'
        endDir = 'E:\\'
        oldFileName = 'events.hdf5'
        #newFileName = params['sub'] + '_TEST' + str(params['runnum']) + '.hdf5'
        #newFileName = 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'] + '.hdf5'
        newFileName = 'nathan.hdf5'
        
        shutil.move(initDir+oldFileName, endDir+newFileName)
        
        print 'File save success!'
        



####### Launch the Experiment #######

runtime=ExperimentRuntime(module_directory(ExperimentRuntime.run), "experiment_config_EyeLink.yaml")
runtime.start()
core.quit()