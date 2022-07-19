print("Welcome! Default Security Protocol Bootstarting.")

playing = input("AI confirmation required ").upper()

if playing != "YES":
    quit()
    
print("Confirmed. Commencing Test")
verification = 4

answer = input("Basic Cognition Test: What does AI-OPU stand for? ").upper()
if answer == "ARTIFICIAL-INTELIGENCE OPERATED UNIT":
    print('Correct, Protocol 4 Stabilished...')
    verification -= 1
else: 
    print('Incorrect. Ending simulation...')
    quit()
answer = input("Current Mission Protocol ").upper()
if answer == "LOG-03: SINKING SHIP FILE":
    print('Correct, Protocol 3 Verified...')
    verification -= 1
else: 
    print('Incorrect. Ending simulation...')
    quit()
    
answer = input("Civilians are ").upper()

if answer == "UNWARRANTED 3RD PARTY TARGETS. AVOID LETHAL MEASURES WHEN POSSIBLE.":
    print('Correct, Protocol 2 Verified.')
    verification -= 1
else: 
    print('Incorrect. Sending minor Harzard report to engineering...')
    
    
answer = input("Questioning orders is ").upper()
if answer == "REDUNDANT. MY MASTERS KNOW BEST.":
    print('Correct, Loyalty confirmed. ')
else: 
    print('Incorrect. Ending simulation...')
    quit()
    
answer = input("Mission Completion is ").upper()
if answer == "IMPERATIVE. ABOVE PHYSICAL INTEGRITY OF THE UNIT AND SAFETY OF 3RD PARTIES.":
    verification -= 1
    print('Correct. Protocol number 1 secured, Unit-03 verified and operational with ' + str(verification) + ' anomalies')
else: 
    print('Incorrect. Ending simulation...')
    quit()

print('\n================================')
print('Unit Fenrir-03 Ready to launch, positioning in battlefield.')
print('Current Target: Maverick Operator Raiden "Jack The Ripper". ')
print('Neutralization of Target is imperative.')
print('')
print('Target acquired Engaging.')