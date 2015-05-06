# The-CSP
Chirag's Superscalar Processor, a 32-bit OOE superscalar processor in SystemVerilog, with assembler, simulator, and a lot more.

Inspired by the ugly mess that is the LC3 and interested by advanced processor architecture, I have created my own processor with additional support material. The CSP is a 32-bit out-of-order execution machine loosely based on the MIPS, Alpha, and i386 architectures.

**ECE Illinois guys: this entire project, especially the software support, may seem similar to what you do in ECE 411. That's because hardware chip development is the same no matter what environment you work in, what company you work for, or what design you work on, and the software tools to aid the designer also generally have the same format. I used the LC3b IDE as support and an idea for the CSP IDE, which is why they may perform and operate very similar (my original idea was a command-line version a la ECE 190/198KL/220)

To facilitate full simulation of this processor, I have written an assembler in Python that inputs a raw assembly file and converts it into CSP-specific machine code that can be read by the processor as memory values. An additional shell script helps automate this entire process. TO also ease assembly programming development, I also wrote an IDE that allows the user to simulate his/her assembly programs before the processor runs them to see if they meet his/her software specs. Finally, a TCL script is added for those who want to synthesize the CSP as a chip, compatible with Synopsys Design Vision.

Breakdown of folders in this repo:
Soft-Processor: Contains all hardware aspects of the CSP. This includes the SystemVerilog code, Quartus additional files, and ModelSim scripts.
Softwares: Contains an assembler, a RAM memory loading script, and the simulation IDE
Doc: Documentation, support of all major files, and other information.
Design: Step-by-step design decisions to help others navigate through the complicated mess that is processor design.
