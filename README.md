# The-CSP
Chirag's Superscalar Processor, a 32-bit OOE superscalar processor in SystemVerilog, with assembler, simulator, and a lot more.

After dealing with the inefficient and ugly mess that is the LC3 and interested with advanced processor architecture since sophomore year, I have created my own processor with additional support material. The CSP is a 32-bit out-of-order execution machine loosely based on the MIPS, Alpha, and i386 architectures.

ECE Illinois guys who stumble here: this entire project, especially the software support, is similar to what you do in ECE 411. That's because hardware chip development is the same no matter what environment you work in, what company you work for, or what design you work on, and the software tools to aid the designer also generally have the same format. I really liked the LC3b's IDE, which is why while taking 411 I wrote the CSP IDE (the previous version was a bloated C++ command-line version a la ECE 190/198KL/220)

To facilitate full simulation of this processor, I have written an assembler in Python that inputs a raw assembly file and converts it into CSP-specific machine code that can be read by the processor as memory values. An additional shell script helps automate this entire process. To also ease assembly programming development, I also wrote an IDE that allows the user to simulate his/her assembly programs before the processor runs them to see if they meet his/her software specs. Finally, since I am after all a die-hard IC designer, I also have some TCL scripts to help in RTL synthesis and physical layout with Synopsys Design Vision and Cadence Encounter (tsmc03d TechLib with the VTVT-250 standard cell library, usually available to most university curricula).

Breakdown of folders in this repo:

Soft-Processor: Contains all hardware aspects of the CSP. This includes the SystemVerilog code, Quartus additional files, and ModelSim scripts.

Softwares: Contains an assembler, a RAM memory loading script, and the simulation IDE

Documentation: Support of all major files, guidelines for programming, and other information.

Design: Step-by-step design decisions to help others navigate through the complicated mess that is processor design.

