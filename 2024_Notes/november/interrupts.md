# interrupts

CPU saves it s current state and jump to a specific routine (interrupt handler)

# what happenes when it occurs ? (exam)

When a task is interrupted, its execution is temporarily halted, and the system takes specific steps to ensure it can resume later without loosing its progress or integrity.

- without saving the state, all data of the program that was being run would be lost

- status 
  - waiting queue
  - ready queue

- Interrupt Service Routine (ISR)
  - signals a higher-priority task requires immiediate attention

- Resuming the interrupted task
  - after ISR completed, system retrives the saved state
  - CPU reloads the saved state and resumes execution of where it has been left