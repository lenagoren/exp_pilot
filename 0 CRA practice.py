#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.03), February 25, 2015, at 21:57
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008

  Changelog 4/23/15:
- separated into three different files

Changelog 10/11/15:
- Added practice file, removed instructions from this into the practice file.
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session (changed to condition for clarity)
expName = 'practice'  # from the Builder filename that created this script
expInfo = {'participant':'', 'condition':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])
#THIS LINE NEEDED FOR WINDOWS

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Setup the Window
win = visual.Window(size=(1280, 1024), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
welcome = visual.TextStim(win=win, ori=0, alignHoriz='center', alignVert='center', name='welcome',
    text=u'Welcome!\n\nIn this experiment, you will be doing a few different tasks, including solving word problems.\n\nFor now, we will teach you how to solve these word problems.',    font=u'Arial',
    pos=[0, 0], height=0.06, wrapWidth=1.5,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "CRA_instruction"
CRA_instructionClock = core.Clock()
CRA_instr1 = visual.TextStim(win=win, ori=0, alignHoriz='center', alignVert='center', name='CRA_instr1',
    text=u'For each problem, you will see three words presented on the screen. \nYou are asked to come up with a solution word that could be combined with each of the three problem words to form a common compound or a phrase. \n\nFor example, what word can go with  \n \npine\ncrab\nsauce',    font=u'Arial',
    pos=[0, 0], height=0.06, wrapWidth=1.5,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "CRA_instruction1"
CRA_instruction1Clock = core.Clock()
CRA_instr2 = visual.TextStim(win=win, ori=0, alignHoriz='center', alignVert='center', name='CRA_instr2',
    text=u'The solution word can precede or follow the problem word.\n\npine apple\ncrab apple\napple sauce',    font=u'Arial',
    pos=[0, 0], height=0.06, wrapWidth=1.5,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "CRA_instruction2"
CRA_instruction2Clock = core.Clock()
insight_instr = visual.TextStim(win=win, ori=0, alignHoriz='center', alignVert='center', name='insight_instr',
    text=u'You will also decide whether the solution was reached with insight or with analysis.\n\nAn insight (similar to an "aha moment") often feels sudden and suprising or as if you "just know" the solution works with all 3 problem words. In addition, you might be unable to articulate how you reached the solution if you solved by insight.',    font=u'Arial',
    pos=[0, 0], height=0.06, wrapWidth=1.5,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
    
# Initialize components for Routine "CRA_instruction2_5"
CRA_instruction2_5Clock = core.Clock()
insight22_instr = visual.TextStim(win=win, ori=0, alignHoriz='center', alignVert='center', name='insight22_instr',
    text=u'Analysis feels more deliberate and you might be more likely to report the steps you took to get to the solution. For example, when you saw the problem \n\npine\ncrab\nsauce\n\n you might have tried to add -apple to all three words one at a time and then test if the compounds produced are valid.',    font=u'Arial',
    pos=[0, 0], height=0.06, wrapWidth=1.5,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "CRA_instruction3"
CRA_instruction3Clock = core.Clock()
CRA_instr3 = visual.TextStim(win=win, ori=0, alignHoriz='center', alignVert='center', name='CRA_instr3',
    text=u'No solution type is better or worse than the other; there are no right or wrong answers in reporting insight or analysis.\n\nThe experimenter will instruct you on the next part of the experiment.',    font=u'Arial',
    pos=[0, 0], height=0.06, wrapWidth=1.5,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "CRA_instruction4"
CRA_instruction4Clock = core.Clock()
CRA_instr4 = visual.TextStim(win=win, ori=0, alignHoriz='center', alignVert='center', name='CRA_instr4',
    text=u'At the beginning of each trial, a \n\n+\n\nwill appear in the center of the screen.',    font=u'Arial',
    pos=[0, 0], height=0.06, wrapWidth=1.5,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "CRA_instruction5"
CRA_instruction5Clock = core.Clock()
CRA_instr5 = visual.TextStim(win=win, ori=0, alignHoriz='center', alignVert='center', name='CRA_instr5',
    text=u"The word problem will appear immediately after the +.\n\nWhen you solve a problem, press the 'spacebar' as soon as you reach a solution. \n\nThen say your solution out loud to the experimenter. ",    font=u'Arial',
    pos=[0, 0], height=0.06, wrapWidth=1.5,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "CRA_instruction6"
CRA_instruction6Clock = core.Clock()
CRA_instr6 = visual.TextStim(win=win, ori=0, alignHoriz='center', alignVert='center', name='CRA_instr6',
    text=u'Then you will be prompted to make your Insight/Analysis judgment using the F or J keys.\n\nF = solved by insight\nJ = solved by analysis',    font=u'Arial',
    pos=[0, 0], height=0.06, wrapWidth=1.5,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "CRA_instruction7"
CRA_instruction7Clock = core.Clock()
CRA_instr7 = visual.TextStim(win=win, ori=0, alignHoriz='center', alignVert='center', name='CRA_instr7',
    text=u'We understand this task is very difficult and don’t be hard on yourself if you don’t find many solutions. \nThere are no right or wrong answers in choosing insight or analysis for your solving method.',    font=u'Arial',
    pos=[0, 0], height=0.06, wrapWidth=1.5,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "CRA_instruction8"
CRA_instruction8Clock = core.Clock()
CRA_instr8 = visual.TextStim(win=win, ori=0, alignHoriz='center', alignVert='center', name='CRA_instr8',
    text=u'We will begin with a few practice problems. \n\nWhen you are ready, please press the spacebar to start the practice trials.',    font=u'Arial',
    pos=[0, 0], height=0.06, wrapWidth=1.5,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Fixation"
FixationClock = core.Clock()
fixation = visual.TextStim(win=win, ori=0, name='fixation',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "CRA_practice"
CRA_practiceClock = core.Clock()
cra_practice = visual.TextStim(win=win, ori=0, name='cra_practice',
    text='bee\ndew\ncomb',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "Solution"
SolutionClock = core.Clock()
cra_solution = visual.TextStim(win=win, ori=0, name='cra_solution',
    text='Solution?',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Ins_or_Ana"
Ins_or_AnaClock = core.Clock()
insight = visual.TextStim(win=win, ori=0, name='insight',
    text=u'Insight (F) or Analysis (J)',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "End_of_task"
End_of_taskClock = core.Clock()
end = visual.TextStim(win=win, ori=0, name='end',
    text='End of task\n\n(Experimenter advance)',    font='Arial',
    pos=[0, 0], height=0.06, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)


#------Prepare to start Routine "Welcome"-------
t = 0
WelcomeClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
advance = event.BuilderKeyResponse()  # create an object of type KeyResponse
advance.status = NOT_STARTED
# keep track of which components have finished
WelcomeComponents = []
WelcomeComponents.append(welcome)
WelcomeComponents.append(advance)
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#-------Start Routine "Welcome"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome* updates
    if t >= 0.0 and welcome.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome.tStart = t  # underestimates by a little under one frame
        welcome.frameNStart = frameN  # exact frame index
        welcome.setAutoDraw(True)
    if welcome.status == STARTED and (0):
        welcome.setAutoDraw(False)
    
    # *advance* updates
    if t >= 0.0 and advance.status == NOT_STARTED:
        # keep track of start time/frame for later
        advance.tStart = t  # underestimates by a little under one frame
        advance.frameNStart = frameN  # exact frame index
        advance.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if advance.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_1'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "CRA_instruction"-------
t = 0
CRA_instructionClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
advance_1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
advance_1.status = NOT_STARTED
# keep track of which components have finished
CRA_instructionComponents = []
CRA_instructionComponents.append(CRA_instr1)
CRA_instructionComponents.append(advance_1)
for thisComponent in CRA_instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "CRA_instruction"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = CRA_instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CRA_instr1* updates
    if t >= 0.0 and CRA_instr1.status == NOT_STARTED:
        # keep track of start time/frame for later
        CRA_instr1.tStart = t  # underestimates by a little under one frame
        CRA_instr1.frameNStart = frameN  # exact frame index
        CRA_instr1.setAutoDraw(True)
    if CRA_instr1.status == STARTED and (0):
        CRA_instr1.setAutoDraw(False)
    
    # *advance_1* updates
    if t >= 0.0 and advance_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        advance_1.tStart = t  # underestimates by a little under one frame
        advance_1.frameNStart = frameN  # exact frame index
        advance_1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if advance_1.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_1'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CRA_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "CRA_instruction"-------
for thisComponent in CRA_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "CRA_instruction1"-------
t = 0
CRA_instruction1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
advance_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
advance_5.status = NOT_STARTED
# keep track of which components have finished
CRA_instruction1Components = []
CRA_instruction1Components.append(CRA_instr2)
CRA_instruction1Components.append(advance_5)
for thisComponent in CRA_instruction1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "CRA_instruction1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = CRA_instruction1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CRA_instr2* updates
    if t >= 0.0 and CRA_instr2.status == NOT_STARTED:
        # keep track of start time/frame for later
        CRA_instr2.tStart = t  # underestimates by a little under one frame
        CRA_instr2.frameNStart = frameN  # exact frame index
        CRA_instr2.setAutoDraw(True)
    if CRA_instr2.status == STARTED and (0):
        CRA_instr2.setAutoDraw(False)
    
    # *advance_5* updates
    if t >= 0.0 and advance_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        advance_5.tStart = t  # underestimates by a little under one frame
        advance_5.frameNStart = frameN  # exact frame index
        advance_5.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if advance_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_1'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CRA_instruction1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "CRA_instruction1"-------
for thisComponent in CRA_instruction1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "CRA_instruction2"-------
t = 0
CRA_instruction2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
advance_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
advance_4.status = NOT_STARTED
# keep track of which components have finished
CRA_instruction2Components = []
CRA_instruction2Components.append(insight_instr)
CRA_instruction2Components.append(advance_4)
for thisComponent in CRA_instruction2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "CRA_instruction2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = CRA_instruction2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *insight_instr* updates
    if t >= 0.0 and insight_instr.status == NOT_STARTED:
        # keep track of start time/frame for later
        insight_instr.tStart = t  # underestimates by a little under one frame
        insight_instr.frameNStart = frameN  # exact frame index
        insight_instr.setAutoDraw(True)
    if insight_instr.status == STARTED and (0):
        insight_instr.setAutoDraw(False)
    
    # *advance_4* updates
    if t >= 0.0 and advance_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        advance_4.tStart = t  # underestimates by a little under one frame
        advance_4.frameNStart = frameN  # exact frame index
        advance_4.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if advance_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_1'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CRA_instruction2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "CRA_instruction2"-------
for thisComponent in CRA_instruction2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "CRA_instruction2_5"-------
t = 0
CRA_instruction2_5Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
advance_88 = event.BuilderKeyResponse()  # create an object of type KeyResponse
advance_88.status = NOT_STARTED
# keep track of which components have finished
CRA_instruction2_5Components = []
CRA_instruction2_5Components.append(insight22_instr)
CRA_instruction2_5Components.append(advance_88)
for thisComponent in CRA_instruction2_5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "CRA_instruction2_5"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = CRA_instruction2_5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *insight_instr* updates
    if t >= 0.0 and insight22_instr.status == NOT_STARTED:
        # keep track of start time/frame for later
        insight22_instr.tStart = t  # underestimates by a little under one frame
        insight22_instr.frameNStart = frameN  # exact frame index
        insight22_instr.setAutoDraw(True)
    if insight22_instr.status == STARTED and (0):
        insight22_instr.setAutoDraw(False)
    
    # *advance_88* updates
    if t >= 0.0 and advance_88.status == NOT_STARTED:
        # keep track of start time/frame for later
        advance_88.tStart = t  # underestimates by a little under one frame
        advance_88.frameNStart = frameN  # exact frame index
        advance_88.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if advance_88.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_1'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CRA_instruction2_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "CRA_instruction2_5"-------
for thisComponent in CRA_instruction2_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
        
#------Prepare to start Routine "CRA_instruction3"-------
t = 0
CRA_instruction3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
advance6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
advance6.status = NOT_STARTED
# keep track of which components have finished
CRA_instruction3Components = []
CRA_instruction3Components.append(CRA_instr3)
CRA_instruction3Components.append(advance6)
for thisComponent in CRA_instruction3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "CRA_instruction3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = CRA_instruction3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CRA_instr3* updates
    if t >= 0.0 and CRA_instr3.status == NOT_STARTED:
        # keep track of start time/frame for later
        CRA_instr3.tStart = t  # underestimates by a little under one frame
        CRA_instr3.frameNStart = frameN  # exact frame index
        CRA_instr3.setAutoDraw(True)
    if CRA_instr3.status == STARTED and (0):
        CRA_instr3.setAutoDraw(False)
    
    # *advance6* updates
    if t >= 0.0 and advance6.status == NOT_STARTED:
        # keep track of start time/frame for later
        advance6.tStart = t  # underestimates by a little under one frame
        advance6.frameNStart = frameN  # exact frame index
        advance6.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if advance6.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_1'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CRA_instruction3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "CRA_instruction3"-------
for thisComponent in CRA_instruction3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "CRA_instruction4"-------
t = 0
CRA_instruction4Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
advance7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
advance7.status = NOT_STARTED
# keep track of which components have finished
CRA_instruction4Components = []
CRA_instruction4Components.append(CRA_instr4)
CRA_instruction4Components.append(advance7)
for thisComponent in CRA_instruction4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "CRA_instruction4"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = CRA_instruction4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CRA_instr4* updates
    if t >= 0.0 and CRA_instr4.status == NOT_STARTED:
        # keep track of start time/frame for later
        CRA_instr4.tStart = t  # underestimates by a little under one frame
        CRA_instr4.frameNStart = frameN  # exact frame index
        CRA_instr4.setAutoDraw(True)
    if CRA_instr4.status == STARTED and (0):
        CRA_instr4.setAutoDraw(False)
    
    # *advance7* updates
    if t >= 0.0 and advance7.status == NOT_STARTED:
        # keep track of start time/frame for later
        advance7.tStart = t  # underestimates by a little under one frame
        advance7.frameNStart = frameN  # exact frame index
        advance7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if advance7.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_1'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CRA_instruction4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "CRA_instruction4"-------
for thisComponent in CRA_instruction4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "CRA_instruction5"-------
t = 0
CRA_instruction5Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
advance8 = event.BuilderKeyResponse()  # create an object of type KeyResponse
advance8.status = NOT_STARTED
# keep track of which components have finished
CRA_instruction5Components = []
CRA_instruction5Components.append(CRA_instr5)
CRA_instruction5Components.append(advance8)
for thisComponent in CRA_instruction5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "CRA_instruction5"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = CRA_instruction5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CRA_instr5* updates
    if t >= 0.0 and CRA_instr5.status == NOT_STARTED:
        # keep track of start time/frame for later
        CRA_instr5.tStart = t  # underestimates by a little under one frame
        CRA_instr5.frameNStart = frameN  # exact frame index
        CRA_instr5.setAutoDraw(True)
    if CRA_instr5.status == STARTED and (0):
        CRA_instr5.setAutoDraw(False)
    
    # *advance8* updates
    if t >= 0.0 and advance8.status == NOT_STARTED:
        # keep track of start time/frame for later
        advance8.tStart = t  # underestimates by a little under one frame
        advance8.frameNStart = frameN  # exact frame index
        advance8.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if advance8.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_1'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CRA_instruction5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "CRA_instruction5"-------
for thisComponent in CRA_instruction5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "CRA_instruction6"-------
t = 0
CRA_instruction6Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
advance9 = event.BuilderKeyResponse()  # create an object of type KeyResponse
advance9.status = NOT_STARTED
# keep track of which components have finished
CRA_instruction6Components = []
CRA_instruction6Components.append(CRA_instr6)
CRA_instruction6Components.append(advance9)
for thisComponent in CRA_instruction6Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "CRA_instruction6"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = CRA_instruction6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CRA_instr6* updates
    if t >= 0.0 and CRA_instr6.status == NOT_STARTED:
        # keep track of start time/frame for later
        CRA_instr6.tStart = t  # underestimates by a little under one frame
        CRA_instr6.frameNStart = frameN  # exact frame index
        CRA_instr6.setAutoDraw(True)
    if CRA_instr6.status == STARTED and (0):
        CRA_instr6.setAutoDraw(False)
    
    # *advance9* updates
    if t >= 0.0 and advance9.status == NOT_STARTED:
        # keep track of start time/frame for later
        advance9.tStart = t  # underestimates by a little under one frame
        advance9.frameNStart = frameN  # exact frame index
        advance9.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if advance9.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_1'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CRA_instruction6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "CRA_instruction6"-------
for thisComponent in CRA_instruction6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "CRA_instruction7"-------
t = 0
CRA_instruction7Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
advance10 = event.BuilderKeyResponse()  # create an object of type KeyResponse
advance10.status = NOT_STARTED
# keep track of which components have finished
CRA_instruction7Components = []
CRA_instruction7Components.append(CRA_instr7)
CRA_instruction7Components.append(advance10)
for thisComponent in CRA_instruction7Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "CRA_instruction7"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = CRA_instruction7Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CRA_instr7* updates
    if t >= 0.0 and CRA_instr7.status == NOT_STARTED:
        # keep track of start time/frame for later
        CRA_instr7.tStart = t  # underestimates by a little under one frame
        CRA_instr7.frameNStart = frameN  # exact frame index
        CRA_instr7.setAutoDraw(True)
    if CRA_instr7.status == STARTED and (0.0):
        CRA_instr7.setAutoDraw(False)
    
    # *advance10* updates
    if t >= 0.0 and advance10.status == NOT_STARTED:
        # keep track of start time/frame for later
        advance10.tStart = t  # underestimates by a little under one frame
        advance10.frameNStart = frameN  # exact frame index
        advance10.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if advance10.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_1'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CRA_instruction7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "CRA_instruction7"-------
for thisComponent in CRA_instruction7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "CRA_instruction8"-------
t = 0
CRA_instruction8Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
begin_practice_CRA = event.BuilderKeyResponse()  # create an object of type KeyResponse
begin_practice_CRA.status = NOT_STARTED
# keep track of which components have finished
CRA_instruction8Components = []
CRA_instruction8Components.append(CRA_instr8)
CRA_instruction8Components.append(begin_practice_CRA)
for thisComponent in CRA_instruction8Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "CRA_instruction8"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = CRA_instruction8Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CRA_instr8* updates
    if t >= 0.0 and CRA_instr8.status == NOT_STARTED:
        # keep track of start time/frame for later
        CRA_instr8.tStart = t  # underestimates by a little under one frame
        CRA_instr8.frameNStart = frameN  # exact frame index
        CRA_instr8.setAutoDraw(True)
    if CRA_instr8.status == STARTED and (0):
        CRA_instr8.setAutoDraw(False)
    
    # *begin_practice_CRA* updates
    if t >= 0.0 and begin_practice_CRA.status == NOT_STARTED:
        # keep track of start time/frame for later
        begin_practice_CRA.tStart = t  # underestimates by a little under one frame
        begin_practice_CRA.frameNStart = frameN  # exact frame index
        begin_practice_CRA.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if begin_practice_CRA.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CRA_instruction8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "CRA_instruction8"-------
for thisComponent in CRA_instruction8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
practice_cra = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'conditions\cra_practice.csv'),
    seed=None, name='practice_cra')
thisExp.addLoop(practice_cra)  # add the loop to the experiment
thisPractice_cra = practice_cra.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPractice_cra.rgb)
if thisPractice_cra != None:
    for paramName in thisPractice_cra.keys():
        exec(paramName + '= thisPractice_cra.' + paramName)

for thisPractice_cra in practice_cra:
    currentLoop = practice_cra
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_cra.rgb)
    if thisPractice_cra != None:
        for paramName in thisPractice_cra.keys():
            exec(paramName + '= thisPractice_cra.' + paramName)
    
    #------Prepare to start Routine "Fixation"-------
    t = 0
    FixationClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FixationComponents = []
    FixationComponents.append(fixation)
    for thisComponent in FixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Fixation"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if t >= 0.0 and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t  # underestimates by a little under one frame
            fixation.frameNStart = frameN  # exact frame index
            fixation.setAutoDraw(True)
        if fixation.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            fixation.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Fixation"-------
    for thisComponent in FixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "CRA_practice"-------
    t = 0
    CRA_practiceClock.reset()  # clock 
    frameN = -1
    routineTimer.add(12.000000)
    # update component parameters for each repeat
    cra_practice.setText(cra.replace(' ','\n'))
    solution_practice = event.BuilderKeyResponse()  # create an object of type KeyResponse
    solution_practice.status = NOT_STARTED
    # keep track of which components have finished
    CRA_practiceComponents = []
    CRA_practiceComponents.append(cra_practice)
    CRA_practiceComponents.append(solution_practice)
    for thisComponent in CRA_practiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "CRA_practice"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CRA_practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *cra_practice* updates
        if t >= 0.0 and cra_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            cra_practice.tStart = t  # underestimates by a little under one frame
            cra_practice.frameNStart = frameN  # exact frame index
            cra_practice.setAutoDraw(True)
        if cra_practice.status == STARTED and t >= (0.0 + (12.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            cra_practice.setAutoDraw(False)
        
        # *solution_practice* updates
        if t >= 0.0 and solution_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            solution_practice.tStart = t  # underestimates by a little under one frame
            solution_practice.frameNStart = frameN  # exact frame index
            solution_practice.status = STARTED
            # keyboard checking is just starting
            solution_practice.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if solution_practice.status == STARTED and t >= (0.0 + (12.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            solution_practice.status = STOPPED
        if solution_practice.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                solution_practice.keys = theseKeys[-1]  # just the last key pressed
                solution_practice.rt = solution_practice.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CRA_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "CRA_practice"-------
    for thisComponent in CRA_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if solution_practice.keys in ['', [], None]:  # No response was made
       solution_practice.keys=None
    # store data for practice_cra (TrialHandler)
    practice_cra.addData('solution_practice.keys',solution_practice.keys)
    if solution_practice.keys != None:  # we had a response
        practice_cra.addData('solution_practice.rt', solution_practice.rt)
    
    if solution_practice.keys == 'space':
        #------Prepare to start Routine "Solution"-------
        t = 0
        SolutionClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        cra_solved = event.BuilderKeyResponse()  # create an object of type KeyResponse
        cra_solved.status = NOT_STARTED
        # keep track of which components have finished
        SolutionComponents = []
        SolutionComponents.append(cra_solution)
        SolutionComponents.append(cra_solved)
        for thisComponent in SolutionComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Solution"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = SolutionClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cra_solution* updates
            if t >= 0.0 and cra_solution.status == NOT_STARTED:
                # keep track of start time/frame for later
                cra_solution.tStart = t  # underestimates by a little under one frame
                cra_solution.frameNStart = frameN  # exact frame index
                cra_solution.setAutoDraw(True)
            if cra_solution.status == STARTED and (0):
                cra_solution.setAutoDraw(False)
            
            # *cra_solved* updates
            if t >= 0.0 and cra_solved.status == NOT_STARTED:
                # keep track of start time/frame for later
                cra_solved.tStart = t  # underestimates by a little under one frame
                cra_solved.frameNStart = frameN  # exact frame index
                cra_solved.status = STARTED
                # keyboard checking is just starting
                cra_solved.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if cra_solved.status == STARTED:
                theseKeys = event.getKeys(keyList=['num_1', 'num_0'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    cra_solved.keys = theseKeys[-1]  # just the last key pressed
                    cra_solved.rt = cra_solved.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SolutionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "Solution"-------
        for thisComponent in SolutionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if cra_solved.keys in ['', [], None]:  # No response was made
           cra_solved.keys=None
        # store data for practice_cra (TrialHandler)
        practice_cra.addData('cra_solved.keys',cra_solved.keys)
        if cra_solved.keys != None:  # we had a response
            practice_cra.addData('cra_solved.rt', cra_solved.rt)
    
        #------Prepare to start Routine "Ins_or_Ana"-------
        t = 0
        Ins_or_AnaClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        insight_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
        insight_resp.status = NOT_STARTED
        # keep track of which components have finished
        Ins_or_AnaComponents = []
        Ins_or_AnaComponents.append(insight)
        Ins_or_AnaComponents.append(insight_resp)
        for thisComponent in Ins_or_AnaComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Ins_or_Ana"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = Ins_or_AnaClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *insight* updates
            if t >= 0.0 and insight.status == NOT_STARTED:
                # keep track of start time/frame for later
                insight.tStart = t  # underestimates by a little under one frame
                insight.frameNStart = frameN  # exact frame index
                insight.setAutoDraw(True)
            
            # *insight_resp* updates
            if t >= 0.0 and insight_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                insight_resp.tStart = t  # underestimates by a little under one frame
                insight_resp.frameNStart = frameN  # exact frame index
                insight_resp.status = STARTED
                # keyboard checking is just starting
                insight_resp.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if insight_resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['f', 'j'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    insight_resp.keys = theseKeys[-1]  # just the last key pressed
                    insight_resp.rt = insight_resp.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Ins_or_AnaComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "Ins_or_Ana"-------
        for thisComponent in Ins_or_AnaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if insight_resp.keys in ['', [], None]:  # No response was made
           insight_resp.keys=None
        # store data for practice_cra (TrialHandler)
        practice_cra.addData('insight_resp.keys',insight_resp.keys)
        if insight_resp.keys != None:  # we had a response
            practice_cra.addData('insight_resp.rt', insight_resp.rt)
        thisExp.nextEntry()
    
# completed 1 repeats of 'practice_cra'

#------Prepare to start Routine "End_of_task"-------
t = 0
End_of_taskClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
advance_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
advance_2.status = NOT_STARTED
# keep track of which components have finished
End_of_taskComponents = []
End_of_taskComponents.append(end)
End_of_taskComponents.append(advance_2)
for thisComponent in End_of_taskComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "End_of_task"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = End_of_taskClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end* updates
    if t >= 0.0 and end.status == NOT_STARTED:
        # keep track of start time/frame for later
        end.tStart = t  # underestimates by a little under one frame
        end.frameNStart = frameN  # exact frame index
        end.setAutoDraw(True)
    if end.status == STARTED and (0):
        end.setAutoDraw(False)
    
    # *advance_2* updates
    if t >= 0.0 and advance_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        advance_2.tStart = t  # underestimates by a little under one frame
        advance_2.frameNStart = frameN  # exact frame index
        advance_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if advance_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_1'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in End_of_taskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "End_of_task"-------
for thisComponent in End_of_taskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

win.close()
core.quit()