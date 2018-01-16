#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.03), February 25, 2015, at 21:57
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
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

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# DEFINE CONDITIONS HERE. ADD DICT FOR EACH CONDITION.
CRASets = {
    'd1': {'real': u'conditions/cra.csv'},
    'd2': {'real': u'conditions/cra_2.csv'}
}

if not (expInfo['condition'] in CRASets):
    raise Exception("Invalid condition ID. Please enter a valid condition code.")

CRAFile = CRASets[expInfo['condition']]

# Setup the Window
win = visual.Window(size=(1280, 1024), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Fixation"
FixationClock = core.Clock()
fixation = visual.TextStim(win=win, ori=0, name='fixation', text='+', font='Arial', pos=[0, 0], height=0.1, wrapWidth=None, color='black', colorSpace='rgb', opacity=1)

# Initialize components for Routine "CRA"
CRAClock = core.Clock()
# for presenting the CRA problems
CRA_problems = visual.TextStim(win=win, ori=0, name='CRA_problems',
    text='dummy', font='Arial', alignHoriz='center',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# CIRCLE, SQUARE, AND TRIANGLE STIM CREATION DEFINED HERE
circle = visual.Circle(win=win, name='circle', radius=0.6, units='cm', edges=32, lineColor='black', lineColorSpace='rgb', fillColor='black', fillColorSpace='rgb', opacity=1, interpolate=True)
square = visual.Rect(win=win, name='square', width=1, height=1, units='cm', lineColor='black', lineColorSpace='rgb', fillColor='black', fillColorSpace='rgb', opacity=1, interpolate=True)
triangle = visual.Polygon(win=win, name='triangle', edges=3, radius=0.7, units='cm', lineColor='black', lineColorSpace='rgb', fillColor='black', fillColorSpace='rgb', opacity=1, interpolate=True)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# THIS IS NEEDED TO CALL THE CORRECT STIM CREATED ABOVE ^ WITHIN THE LOOP BELOW (CRA_distractor component)
# Since you needed it to loop through several different distractors in the length of the CRA (after onset of distractor time), I have it so the distractors are now conditions consisting of lists of distractors. Change as necessary (and make the appropriate changes in the CSV as well).
CRA_dist_list = {'cstct': [circle, square, triangle, circle, triangle, square],
                  'sctcs': [square, circle, triangle, circle, square, triangle],
                  'tscst': [triangle, square, circle, square, triangle, circle]
                  }

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# THIS IS NEEDED TO CREATE THE POSITIONS.
CRA_pos_list = {'pos1': [[-6, 6], [6, -6], [-6, 6], [-6, -6],[-6, 6], [-6, -6]],
                'pos2': [[6, -6], [-6, 6], [-6, 6], [-6, -6],[-6, 6], [-6, -6]],
                'pos3': [[6, -6], [-6, 6], [6, -6], [-6, -6],[6, -6], [-6, -6]]
}

# Initialize components for Routine "Solution"
SolutionClock = core.Clock()
cra_solution = visual.TextStim(win=win, ori=0, name='cra_solution',
    text='Solution?',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1)

# Initialize components for Routine "Ins_or_Ana"
Ins_or_AnaClock = core.Clock()
insight = visual.TextStim(win=win, ori=0, name='insight',
    text=u'Insight (F) or Analysis (J)',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1)

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
blank = visual.TextStim(win=win, ori=0, name='blank',
    text=None,    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1)

# Initialize components for Routine "End_of_task"
End_of_taskClock = core.Clock()
end = visual.TextStim(win=win, ori=0, name='end',
    text='End of task\n\n(Experimenter advance)',    font='Arial',
    pos=[0, 0], height=0.06, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1)
    
# set up handler to look after randomisation of conditions etc
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# THIS IS THE CRA LOOP HANDLER. YOU CAN CHANGE EVERYTHING EXCEPT THE TRIALLIST, WHICH READS THE CSV (DEFINED NEAR TOP)
# set up handler to look after randomisation of conditions etc
CRA_pt1 = data.TrialHandler(nReps=1, method='sequential',
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(CRAFile['real']),
    seed=None, name='CRA_pt1')
thisExp.addLoop(CRA_pt1)  # add the loop to the experiment
thisCRA_pt1 = CRA_pt1.trialList[0]  # so we can initialise stimuli with some values

if thisCRA_pt1 != None:
    for paramName in thisCRA_pt1.keys():
        exec(paramName + '= thisCRA_pt1.' + paramName)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ACTUAL LOOP BEGINS HERE
for thisCRA_pt1 in CRA_pt1:
    currentLoop = CRA_pt1
    # abbreviate parameter names if possible (e.g. rgb = thisCRA_pt1.rgb)
    if thisCRA_pt1 != None:
        for paramName in thisCRA_pt1.keys():
            exec(paramName + '= thisCRA_pt1.' + paramName)

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

    # ------Prepare to start Routine "CRA"-------
    t = 0
    CRAClock.reset()  # clock
    frameN = -1
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Total amount of time to show CRAs
    routineTimer.add(12.000000)
    # update component parameters for each repeat

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # THIS UPDATES THE CRA EACH LOOP BASED ON WHAT'S IN THE CSV
    CRA_problems.setText(cra.replace(' ', '\n'))

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # THIS CREATES THE DISTRACTOR SHAPE IF THE DISTRACTOR FOR N-TRIAL IS NOT BOLD
    if stim != 'bold':

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # CRA stims are now conditions which are lists of a sequence of distractors; the distractors will need to be looped.
        # Please make sure the distractors are defined in the condition above and in the CSV.
        # Pre-load first distractor so psychopy will be ready to draw it.
        # Keep track of stim number here, to be updated each loop (after distractor "off")
        stim_num = 0
        CRA_distractor = CRA_dist_list[stim][stim_num]

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # Pre-load first position so psychopy will be ready to draw it.
        # Keep track of position number here, to be updated each loop (after distractor "off")
        pos_num = 0
        CRA_distractor.pos = CRA_pos_list[position][pos_num]

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        # How long between distractors
        offTime = distTime + 1.0

    solution_cra = event.BuilderKeyResponse()  # create an object of type KeyResponse
    solution_cra.status = NOT_STARTED
    # keep track of which components have finished
    CRAComponents = []
    CRAComponents.append(CRA_problems)
    CRAComponents.append(CRA_distractor)
    CRAComponents.append(solution_cra)

    for thisComponent in CRAComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "CRA"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CRAClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # THIS SHOWS EVERY CRA PROBLEM AT PROBLEM ONSET (DON'T TOUCH THIS)
        # *CRA_problems* updates
        if t >= 0.0 and CRA_problems.status == NOT_STARTED:
            # keep track of start time/frame for later
            CRA_problems.tStart = t  # underestimates by a little under one frame
            CRA_problems.frameNStart = frameN  # exact frame index
            CRA_problems.setAutoDraw(True)

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # THIS BOLDS THE CRA IF THE TRIAL STATES IT SHOULD BE BOLDED.
        if stim == 'bold':
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # IT BOLDS THE CRA AT ONSET TIME (DISTTIME).
            if t >= distTime and CRA_problems.status == STARTED:
                CRA_problems.bold = True

            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # STOPS BOLDING THE CRA AFTER ONE SECOND. CHANGE 1.0 TO ANY AMOUNT OF TIME.
            # TO CHECK IF YOUR TIMING IS ACCURATE, YOU CAN USE: print CRAClock.getTime()
            if CRA_problems.status == STARTED and t >= (
                distTime + (1.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
                CRA_problems.bold = False
                distTime = distTime + 2.0

        else:
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # THIS IS FOR THE SHAPE DISTRACTORS. IT WILL ONLY DRAW THEM AFTER ONSET TIME (DISTTIME)
            # First, draw first distractor at onset time (distTime)
            # onset at distTime
            if (t >= distTime):
                # keep track of start time/frame for later
                CRA_distractor.tStart = t  # underestimates by a little under one frame
                CRA_distractor.frameNStart = frameN  # exact frame index
                CRA_distractor.setAutoDraw(True)
                CRA_distractor.status = STARTED

            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # STOPS SHOWING DISTRACTOR AFTER ONE SECOND. YOU CAN CHANGE 1.0 TO ANY TIME ABOVE.
            if (t >= offTime):  # most of one frame period left
                CRA_distractor.setAutoDraw(False)
                # Only increments distTime, offTime, stims, and positions when offTime is less than 12 (so you don't get a distTime at 12.0 or larger).
                if (offTime + 2.0) <= 12.0:
                    distTime = distTime + 2.0
                    offTime = offTime + 2.0
                    stim_num = stim_num + 1
                    pos_num = pos_num + 1
                    CRA_distractor = CRA_dist_list[stim][stim_num]
                    CRA_distractor.pos = CRA_pos_list[position][pos_num]
                CRA_distractor.status = NOT_STARTED

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # if 12s have elapsed, stop drawing CRA
        if CRA_problems.status == STARTED and t >= (
            0.0 + (12.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            CRA_problems.setAutoDraw(False)

        # *solution_cra* updates
        if t >= 0.0 and solution_cra.status == NOT_STARTED:
            # keep track of start time/frame for later
            solution_cra.tStart = t  # underestimates by a little under one frame
            solution_cra.frameNStart = frameN  # exact frame index
            solution_cra.status = STARTED
            # keyboard checking is just starting
            solution_cra.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if solution_cra.status == STARTED and t >= (
            0.0 + (12.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            solution_cra.status = STOPPED
        if solution_cra.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            solution_cra.keys = theseKeys[-1]  # just the last key pressed
            solution_cra.rt = solution_cra.clock.getTime()
            # a response ends the routine
            continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CRAComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "CRA"-------
    for thisComponent in CRAComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

            # !!!!!!!!!!!!!!!!!!!!!
            # Needed to reset stim or bold after problem ends
            CRA_problems.bold = False
            CRA_distractor.status = NOT_STARTED
            CRA_distractor.setAutoDraw(False)

    # check responses
    if solution_cra.keys in ['', [], None]:  # No response was made
        solution_cra.keys = None
    # store data for CRA_pt1 (TrialHandler)
    CRA_pt1.addData('solution_cra.keys', solution_cra.keys)
    if solution_cra.keys != None:  # we had a response
        CRA_pt1.addData('solution_cra.rt', solution_cra.rt)

    if solution_cra.keys == 'space':
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
                theseKeys = event.getKeys(keyList=['1', '2'])

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
        # store data for CRA_pt1 (TrialHandler)
        CRA_pt1.addData('cra_solved.keys',cra_solved.keys)
        if cra_solved.keys != None:  # we had a response
            CRA_pt1.addData('cra_solved.rt', cra_solved.rt)

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
        # store data for CRA_pt1 (TrialHandler)
        CRA_pt1.addData('insight_resp.keys',insight_resp.keys)
        if insight_resp.keys != None:  # we had a response
            CRA_pt1.addData('insight_resp.rt', insight_resp.rt)

    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = []
    ISIComponents.append(blank)
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "ISI"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *blank* updates
        if t >= 0.0 and blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank.tStart = t  # underestimates by a little under one frame
            blank.frameNStart = frameN  # exact frame index
            blank.setAutoDraw(True)
        if blank.status == STARTED and t >= (
            0.0 + (np.random.random_integers(2, 3) - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            blank.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
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

    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()

# completed 1 repeats of 'CRA_pt1'

# ------Prepare to start Routine "End_of_task"-------
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

# -------Start Routine "End_of_task"-------
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
        theseKeys = event.getKeys(keyList=['1'])

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

# -------Ending Routine "End_of_task"-------
for thisComponent in End_of_taskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

win.close()
core.quit()