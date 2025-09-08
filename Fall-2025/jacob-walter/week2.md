The only thing i am unsure about at the moment if bitwise operations on FP16 are any different than on any other format, and that is only cause i was assigned it right before i am writing this. Also could use a bit more specifics on the FUs but i will probably get that on sunday.


Vector Core Meeting Notes:
Was introduced to the project
immediate responsibilities: FP16 XOR and NOT, Reduction FUs, maybe some other FUs.
potential later responsibilites (if i understand them correctly): integration with scoreboard and work with software

Planned timeframe:
FP16 XOR and NOT finished by end of sunday
FUs done in around 2-3 weeks.
I think we are planned for verifictaion in late september/early october


Main Socet meeting notes:
Listened to people talk about their internships.
Seems that this will be useful for getting a job.
Heard some nice things that will be useful, and i should probably look into non python scripting.

Time Worked: About 2.5 hours

What I did:
Got the development environment setup and looked through the repository to understand project structure
Done some reseach about FP16 and if it has any special bitwise operations. It seems like it doesnt but i will ask to make sure.
Did some basic reasearch about vector reductions and batcehd vector reductions. I need to get some actual specifics on what vector reduction operations we will need, but theoretically the FU doesnt look like it will be too bad for implamentation.