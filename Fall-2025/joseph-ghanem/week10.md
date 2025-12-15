
State: Not stuck on anything

# Progress
1) VRF Cacti modeling 
- The issue with the VRF is that it is extremely area inefficient. The incredidly long register sizes blows up area as SRAM requires drivers for the word lines, extra bit lines and sense amps, etc. Subbanking is an option explored to partition the banks into sub banks to limit this inefficiency. Cacti confirmed this theory as the banks with the sub banks were notably more area effecient and took up less area

2) Recalculating VRF area
- resynthesized VRF area and vbank area, took total area - 4*vbank_area + 4*cacti_bank_estimate to get the estimated VRF area on 90nm which is about ~1.3mm^2. This may seem large given the 3.5mm^2 vector core area constraint although the VRF in vector processors is typically alloted 40-60% of area and power budget so it is okay. 


# Future Plans
- pcacti 
- lane unit