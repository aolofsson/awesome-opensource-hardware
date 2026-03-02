# awesome-opensource-hardware

A curated list of awesome open source hardware tools, generators, and reusable designs.

* Categorized
* Alphabetical (per category)
* Requirements
  - link should be to source code repository
  - open source projects only
  - working projects only (not WIP/rusty)
* One tag line sentence per project

# Table of Contents

## PDKs
   * [Manufacturable PDKs](#manufacturable-pdks)
   * [Virtual PDKs](#virtual-pdks)

## Compilers
  * [Build systems](#build-systems)
  * [Circuit compilers](#circuit-compilers)
  * [FPGA compilers](#fpga-compilers)
  * [Layout compilers](#layout-compilers)

## Project
  * [Documentation](#documentation)

## Design and Verification Tools
  * [Benchmarks](#benchmarks)
  * [Board design](#board-design)
  * [Digital design](#digital-design)
  * [FPGA design](#fpga-design)
  * [Formal verification](#formal-verification)
  * [Linters](#linters)
  * [Register design](#register-design)
  * [Schematics](#scehamtics)
  * [Simulators](#simulators)
  * [Verification frameworks](#verification-frameworks)
  * [Physics](#physics)
  * [Waveform Viewers](#waveform-viewers)

## Designs & Generators
  * [Accelerators](#accelerators)
  * [AIB](#aib)
  * [AXI](#axi)
  * [Analog circuits](#analog-circuits)
  * [Chip packaging](#chip-packages)
  * [Boards](#board-designs)
  * [Connectivity](#connectivity)
  * [CPUs](#cpus)
  * [FPGA architectures](#fpga-architectures)
  * [Libraries](#libraries)
  * [Memory](#memory)
  * [Systems](#systems)

## Education
  * [Analog design](#analog-design)
  * [ASIC design](#asic-design)
  * [Digital design](#digital-design)
  * [FPGA design](#fpga-design)

# PDKs

## Manufacturable PDKs

* [gf180](https://github.com/google/gf180mcu-pdk)
  * GlobalFoundries 180nm CMOS PDK
* [sg13g2](https://github.com/IHP-GmbH/IHP-Open-PDK)
  * IHP 130nm BiCMOS PDK
* [sky130](https://github.com/google/skywater-pdk)
  * Skywater 130nm CMOS PDK

## Virtual PDKs
* [asap7](https://github.com/The-OpenROAD-Project/asap7)
  * Predictive 7nm PDK
* [freepdk45](https://github.com/siliconcompiler/siliconcompiler/tree/main/third_party/pdks/virtual/freepdk45)
  * Predictive 45nm PDK
* [probe3.0](https://github.com/ABKGroup/PROBE3.0)
  * Process/design DTCO path finding technology

# AI

* [AnalogCoder](https://github.com/laiyao1/AnalogCoder)
 * Analog Circuit Design via Training-Free Code Generation
* [hagent](https://github.com/masc-ucsc/hagent)
 * hardware agent
* [Masala-CHAI](https://github.com/jitendra-bhandari/Masala-CHAI)
 * Large-Scale SPICE Netlist Dataset for Analog Circuits



# Compilers

## Build Systems
* [bazelhdl](https://github.com/hdl/bazel_rules_hdl)
  * Bazel based hdl build system
* [bender](https://github.com/pulp-platform/bender)
  * Dependency management tool for hardware projects.
* [chipyard](https://github.com/ucb-bar/chipyard)
  * Agile RISC-V SoC Design Framework.
* [cocoon](https://github.com/pku-dasys/cocoon)
  * Infrastructure for integrated EDA
* [edalize](https://github.com/olofk/edalize)
  * Abstraction library for interfacing EDA tools.
* [flgen](https://github.com/pezy-computing/flgen)
  * Generate a filelist for EDA tools
* [fusesoc](https://github.com/olofk/fusesoc)
  * Package manager and build abstraction tool for FPGA/ASIC development.
* [hammer](https://github.com/ucb-bar/hammer)
  * Agile physical design component part of UC Berkeley Chipyard framework.
* [hbs](https://github.com/m-kru/hbs)
  * Tcl-based, minimal common abstraction build system for hardware design projects.
* [hwtbuildsystem](https://github.com/Nic30/hwtBuildsystem)
  * Library of utils for interaction with the vendor tools.
* [mflowgen](https://github.com/mflowgen/mflowgen)
  * Build-system generator for ASIC and FPGA design-space exploration.
* [orbit](https://github.com/chaseruskin/orbit)
  * Package manager and build tool for HDLs
* [siliconcompiler](https://github.com/siliconcompiler/siliconcompiler)
  * Python based build system and package manager for hardware.
* [SoCMake](https://github.com/HEP-SoC/SoCMake)
  * Hardware and software build system and package manager based on CMake

## Circuit Compilers
* [abc](https://github.com/berkeley-abc/abc)
  * System for sequential logic synthesis and formal verification
* [act](https://github.com/asyncvlsi/act)
  * Asynchronous circuit compiler tools
* [aihwkit](https://github.com/IBM/aihwkit)
  * IBM Analog Hardware Acceleration Kit
* [amaranth](https://github.com/amaranth-lang/amaranth)
  * Python based hardware design framework
* [bigspicy](https://github.com/google/bigspicy)
  * Tool for merging circuit descriptions
* [bsc](https://github.com/B-Lang-org/bsc)
  * Compiler, simulator, and tools for the Bluespec Hardware Description Language
* [calyx](https://github.com/cucapra/calyx)
  * Intermediate language and compilers that generate custom hardware accelerators
* [chisel](https://github.com/chipsalliance/chisel3)
  * Scala based hardware description language
* [circt](https://github.com/llvm/circt)
  * Circuit IR Compilers and Tools
* [circuitgraph](https://github.com/circuitgraph/circuitgraph)
  * Tools for working with circuits as graphs in python
* [circuitops](https://github.com/NVlabs/CircuitOps)
  * Infrastructure for dataset generation and model deployment in Generative AI
* [clash](https://github.com/clash-lang/clash-compiler)
  * Haskell to VHDL/Verilog/SystemVerilog compiler
* [coreir](https://github.com/rdaly525/coreir)
  * LLVM-style hardware compiler with first class support for generators
* [dfiant](https://github.com/DFiantHDL/DFiant)
  * Dataflow Hardware Description Language
* [fault](https://github.com/AUCOHL/Fault)
  * Design-for-testing (DFT) Solution
* [finn](https://github.com/Xilinx/finn)
  * Dataflow compiler for QNN inference
* [firrtl](https://github.com/chipsalliance/firrtl)
  * Intermediate Representation for RTL
* [gamma](https://github.com/maestro-project/gamma)
  * Optimizes mapping of DNN models on DNN Accelerators
* [gamora](https://github.com/Yu-Utah/Gamora)
  * Graph Learning based Symbolic Reasoning for Large-Scale Boolean Networks
* [ghdl-yosys-plugin](https://github.com/ghdl/ghdl-yosys-plugin)
  * VHDL synthesis (based on ghdl)
* [halide](https://github.com/halide/Halide)
  * Language for fast, portable data-parallel computation
* [halide-to-hardware](https://github.com/StanfordAHA/Halide-to-Hardware)
  * Hardware generator combining halide and coreir
* [hastlayer](https://github.com/Lombiq/Hastlayer-SDK)
  * VHDL generator from .NET languages (C#, F#, and others) and FPGA framework for .NET hardware acceleration
* [hdl21](https://github.com/dan-fritchman/Hdl21)
  * Hardware Description Library
* [hdlconvertor](https://github.com/Nic30/hdlConvertor)
  * Verilog/VHDL parser preprocessor and code generator for C++/Python based on ANTL4
* [hs-to-coq](https://github.com/plclub/hs-to-coq)
  * Convert Haskell source code to Coq source code
* [ipyxact](https://github.com/olofk/ipyxact)
  * Python-based IP-XACT parser
* [livehd](https://github.com/masc-ucsc/livehd)
  * Infrastructure for live interactive synthesis and simulation
* [llhd](https://github.com/fabianschuiki/llhd)
  * Intermediate representation for digital circuit descriptions
* [lsoracle](https://github.com/lnis-uofu/LSOracle)
  * Famework built on EPFL logic synthesis libraries.
* [lstools](https://github.com/lsils/lstools-showcase)
  * Showcase examples for EPFL logic synthesis libraries
* [kami](https://github.com/mit-plv/kami)
  * Platform for High-Level Parametric Hardware Specification and Verification
* [magma](https://github.com/phanrahan/magma/)
  * Python based hardware design language
* [matchlib](https://github.com/NVlabs/matchlib)
  * Synthesizable SystemC/C++ library of commonly-used hardware functions
* [matchclib_connections](https://github.com/hlslibs/matchlib_connections)
  * Synthesizable SystemC library implementing latency-insensitive channels
* [mockturtle](https://github.com/lsils/mockturtle)
  * C++ logic network library
* [myhdl](https://github.com/myhdl/myhdl)
  * Python based hardware description and verification language
* [naja](https://github.com/xtofalex/naja)
  * Structural Netlist API for EDA post synthesis flow development
* [netlist-paths](https://github.com/jameshanlon/netlist-paths)
  * A library and command-line tool for querying a Verilog netlist
* [panda-bambu](https://github.com/ferrandi/PandA-bambu)
  * High level synthesis (HLS) C/C++ framework
* [pipelinec](https://github.com/JulianKemmerer/PipelineC)
  * C-like hardware description language (HDL) with automatic pipelining
* [pygears](https://github.com/bogdanvuk/pygears)
  * Python based hardware design framework
* [pymtl3](https://github.com/pymtl/pymtl3)
  * Python hardware generation, simulation, and verification framework
* [pyrtl](https://github.com/UCSBarchlab/PyRTL)
  * Python integrated design and simulation framework
* [pysysc](https://github.com/accellera-official/PySysC)
  * Python package to make SystemC usable from Python
* [pyverilog](https://github.com/PyHDI/Pyverilog)
  * Python design toolkit for Verilog HDL
* [rohd](https://github.com/intel/rohd)
  * Dart based framework for describing and verifying hardware
* [scip](https://github.com/scipopt/scip)
  * Solving Constraint Integer Problems
* [silice](https://github.com/sylefeb/Silice)
  * Language that simplifies prototyping and writing algorithms on FPGA architectures
* [skidl](https://github.com/devbisme/skidl)
  * SKiDL is a module that extends Python with the ability to design electronic circuits
* [slang](https://github.com/MikePopoloski/slang)
  * Library for lexing, parsing, type checking, and elaborating SystemVerilog code
* [sodaopt](https://github.com/pnnl/soda-opt)
  * Optimizer leveraging mlir to extract, optimize, translate HLSinto LLVM IR
* [spinalhdl](https://github.com/SpinalHDL/SpinalHDL)
  * Scala based HDL
* [spydrnet](https://github.com/byuccl/spydrnet)
  * Framework for analyzing and transforming Verilog netlists
* [surelog](https://github.com/chipsalliance/Surelog)
  * SystemVerilog IEEE 2017 Pre-processor, Parser, Elaborator, UHDM Compiler
* [sv-parser](https://github.com/dalance/sv-parser)
  * SystemVerilog IEEE 1800-2017 parser library
* [sv2v](https://github.com/zachjs/sv2v)
  * SystemVerilog to Verilog conversion
* [systemc](https://github.com/accellera-official/systemc)
  * SystemC system design and verification language that spans hardware and software
* [systemc-compiler](https://github.com/intel/systemc-compiler)
  * Translates synthesizable SystemC to synthesizable Verilog
* [synlig](https://github.com/chipsalliance/synlig)
  * SystemVerilog support for Yosys
* [tapasco](https://github.com/esa-tu-darmstadt/tapasco)
  * Heterogeneous system composer
* [tce](https://github.com/cpc/tce)
  * Application-specific instruction-set processor (ASIP) toolset
* [uhdm](https://github.com/chipsalliance/UHDM)
  * Universal object model for IEEE SystemVerilog designs
* [verible](https://github.com/chipsalliance/verible)
  * SystemVerilog developer tools, including a parser, style-linter, and formatter
* [veriloggen](https://github.com/PyHDI/veriloggen)
  * Mixed-Paradigm Hardware Construction Framework
* [veryl](https://github.com/veryl-lang/veryl)
  * Modern Hardware Description Language based on Rust/SV
* [verik](https://github.com/frwang96/verik)
  * Kotlin based hardware description language
* [vlsir](https://github.com/Vlsir/Vlsir)
  * Interchange formats for chip design
* [xls](https://github.com/google/xls)
  * Google framework for hardware synthesis
* [yosys](https://github.com/YosysHQ/yosys)
  * Yosys Open SYnthesis Suite

## FPGA Compilers

* [amf-placer](https://github.com/zslwyuan/AMF-Placer)
  * Timing-driven analytical mixed-size FPGA placer
* [dreamplacefpga](https://github.com/rachelselinar/DREAMPlaceFPGA)
  * Analytical Placer for Large Scale Heterogeneous FPGA
* [flowtune](https://github.com/Yu-Utah/FlowTune)
  * FPGA synehsis and PNR optimizer
* [nextpnr](https://github.com/YosysHQ/nextpnr)
  * FPGA place and route tool
* [vtr](https://github.com/verilog-to-routing/vtr-verilog-to-routing)
  * FPGA place and route tool

## Layout Compilers

* [align](https://github.com/ALIGN-analoglayout/ALIGN-public)
  * Automatic layout generator for analog circuits
* [autodmp](https://github.com/NVlabs/AutoDMP)
  * Automated DREAMPlace-based Macro Placement
* [bag](https://github.com/ucb-art/BAG_framework)
  * Berkeley analog layout generator
* [coriolis](https://gitlab.lip6.fr/vlsi-eda/coriolis.git)
  * RTL2GDS toolchain for mature nodes
* [dreamplace](https://github.com/limbo018/DREAMPlace)
  * Deep learning toolkit-enabled VLSI placement
* [gdsfactory](https://github.com/gdsfactory/gdsfactory)
  * Platform for chip design and layout
* [gds3d](https://github.com/trilomix/GDS3D)
  * Render GDS files in 3D
* [gdsiistl](https://github.com/dteal/gdsiistl)
  * Converts GDSII files to STL files
* [gdstk](https://github.com/heitzmann/gdstk)
  * C++/Python library for creation and manipulation of GDSII and OASIS files.
* [gdspy](https://github.com/heitzmann/gdspy)
  * Python module for creating GDSII stream files, usually CAD layouts.
* [ieda](https://github.com/OSCC-Project/iEDA)
  * RTL2GDS infrastructure
* [klayout](https://github.com/KLayout/klayout)
  * Layout viewer
* [kweb](https://github.com/gdsfactory/kweb)
  * Klayout Web Viewer
* [lclayout](https://codeberg.org/librecell/lclayout)
  * Layout generator for CMOS standard-cells
* [layout21](https://github.com/dan-fritchman/Layout21)
  * Integrated Circuit Layout
* [magic](https://github.com/RTimothyEdwards/magic)
  * Magic VLSI layout tool
* [magical](https://github.com/magical-eda/MAGICAL)
  * Machine Generated Analog IC Layout
* [openroad](https://github.com/The-OpenROAD-Project/OpenROAD)
  * Complete RTL2GDS platform
* [phidl](https://github.com/amccaugh/phidl)
  * Python GDS layout and CAD geometry creation


# Design and Verification Tools

## Benchmarks
* [big-doe-openroad](https://github.com/msaligane/Big-DoE-OpenROAD)
  * Framework for launching massive RTL2GDS experiements
* [bringup-bench](https://github.com/toddmaustin/bringup-bench)
  * Collection of minimal programs useful for system bringup
* [bsg_pipeclean_suite](https://github.com/bespoke-silicon-group/bsg_pipeclean_suite)
  * Collection of designs used to stress test new CAD flows
* [corescore](https://github.com/olofk/corescore)
  * Benchmark for FPGAs and their synthesis/P&R tools
* [epfl-benchmarks](https://github.com/lsils/benchmarks)
  * Combinational Benchmark Suite for logic synthesis
* [fpga-tool-perf](https://github.com/chipsalliance/fpga-tool-perf)
  * FPGA tool performance profiling
* [opdb](https://github.com/PrincetonUniversity/OPDB)
  * Princeton design benchmark generators
* [rdf-2020](https://github.com/ieee-ceda-datc/RDF-2020)
  * IEEE CEDA eda benchmark flow
* [sv-tests](https://github.com/chipsalliance/sv-tests)
  * SystemVerilog compliance test suite
* [verilog-eval](https://github.com/NVlabs/verilog-eval)
  * Verilog evaluation benchmark for large language model

## Board Design
* [boardview](https://github.com/whitequark/kicad-boardview)
  * Reads KiCAD PCB layout files and writes ASCII Boardview files
* [cuflow](https://github.com/jamesbowman/cuflow)
  * Experimental procedural PCB layout program
* [datasheet-scrubber](https://github.com/idea-fasoc/datasheet-scrubber)
  * Scrubs PDF datasheets/documents in order to extract key circuit information
* [freecad](https://github.com/FreeCAD/FreeCAD)
  * 3D parametric CAD system
* [freerouting](https://github.com/freerouting/freerouting)
  * PCB auto-router
* [kicad](https://github.com/KiCad/kicad-source-mirror)
  * Board design framework
* [kicad-skip](https://github.com/psychogenic/kicad-skip)
  * kicad s-expression schematic/layout file manipulation
* [kicanvas](https://github.com/theacodes/kicanvas)
  * KiCAD web viewer
* [kicad-footprint-generator](https://gitlab.com/kicad/libraries/kicad-footprint-generator)
  * kicad footprint generator using python scripts
* [kicad-library-utils](https://gitlab.com/kicad/libraries/kicad-library-utils)
  * scripts for helping with library development
* [kikit](https://github.com/yaqwsx/KiKit)
  * Automation tools for kicad
* [librepcb](https://github.com/LibrePCB/LibrePCB)
  * Board design framework
* [pcbflow](https://github.com/michaelgale/pcbflow)
  * Python based Printed Circuit Board (PCB) layout and design package based on CuFlow

## Digital Design
* [digital](https://github.com/hneemann/Digital)
  * Digital logic designer and circuit simulator
* [DigSim](https://github.com/freand76/digsim)
  * An interactive digital logic simulator with verilog support (Yosys)
* [verilog-mode](https://www.veripool.org/verilog-mode/)
  * Popular free Verilog mode for Emacs
* [vsrtl](https://github.com/mortbopet/VSRTL/)
  * Visual Simulation of Register Transfer Logic
* [vscode-systemverilog](https://github.com/eirikpre/VSCode-SystemVerilog)
  * SystemVerilog support in VS Code
* [vscode-teroshdl](https://github.com/TerosTechnology/vscode-terosHDL)
  * Full IDE for RTL development in VS Code

## Documentation
* [elk](https://github.com/eclipse/elk)
  * Eclipse Layout Kernel - Automatic layout for Java applications.
* [graphviz](https://github.com/xflr6/graphviz)
  * Python library for graph cration and rendering in DOT language
* [gds3d](https://github.com/trilomix/GDS3D)
  * Reads GDSII layout and renders in 3D
* [hdelk](https://github.com/davidthings/hdelk)
  * Web-based HDL diagramming tool
* [kythe](https://github.com/chipsalliance/verible/blob/master/verilog/tools/kythe)
  * Verible based SystemVerilog source file indexer
* [memory-layout-diagram](https://github.com/gerph/memory-layout-diagram)
  * Diagrams for memory map layouts
* [netlistsvg](https://github.com/nturley/netlistsvg)
  * Draws an SVG schematic from a JSON netlist
* [netlist-viewer](https://github.com/f18m/netlist-viewer)
  * SPICE netlist visualizer
* [nn-svg](https://github.com/alexlenail/NN-SVG)
  * Publication-ready NN-architecture schematics
* [pcbdraw](https://github.com/yaqwsx/PcbDraw)
  * Convert KiCAD board into 2D drawing suitable for pinout diagrams
* [pinion](https://github.com/yaqwsx/Pinion)
  * Generate interactive Diagrams for your PCBs
* [pinout](https://github.com/j0ono0/pinout)
  * Python package that generates hardware pinout diagrams as SVG images
* [sphinx](https://github.com/sphinx-doc/sphinx)
  * Document builder
* [sphinx-verilog-domain](https://github.com/SymbiFlow/sphinx-verilog-domain)
  * Sphinx package for integration SystemVerilog documentation into Sphinx.
* [sphinxcontrib-hdl-diagrams](https://github.com/SymbiFlow/sphinxcontrib-hdl-diagrams)
  * Sphinx plugin to automatically generate diagrams from RTL.
* [symbolator](https://github.com/kevinpt/symbolator)
  * HDL symbol generator
* [undulate](https://github.com/LudwigCRON/undulate)
  * Python compatible wavedrom module with extensions and console rendering support
* [wavedrom](https://github.com/wavedrom/wavedrom)
  * Digital timing diagram rendering engine
* [wavedrompy](https://github.com/wallento/wavedrompy)
  * Python comptabled Wavedrom module
* [wireviz](https://github.com/wireviz/WireViz)
  * Docuyment cables and wiring harnesses


## FPGA Design
* [byteman](https://github.com/FPGA-Research-Manchester/byteman)
  * Bitstream relocation and manipulation tool
* [icestudio](https://github.com/FPGAwars/icestudio)
  * Visual editor for open FPGA boards
* [f4fpga](https://github.com/chipsalliance/f4pga)
  * FPGA toolchain
* [f4pga/f4pga-arch-defs](https://github.com/f4pga/f4pga-arch-defs)
  * FPGA architecture definitions for F4FPGA
* [foedag](https://github.com/os-fpga/FOEDAG)
  * Framework Open EDA Gui
* [logik](https://github.com/zeroasiccorp/logik)
  * FPGA toolchain
* [openfpgaloader](https://github.com/trabucayre/openFPGALoader)
  * Universal utility for programming FPGA
* [pyfpga](https://github.com/PyFPGA/pyfpga)
  * Python based FPGA compilation
* [rphax](https://github.com/shariethernet/RPHAX)
  * Automation flow to develop and prototype hardware accelerators on Xilinx FPGAs

## Formal Verification
* [boolector](https://github.com/boolector/boolector)
  * SMT solver for tfixed-size bit-vectors, arrays and uninterpreted functions
* [cvc5](https://github.com/cvc5/cvc5)
  * SMT automatic theorem prover
* [ilang](https://github.com/PrincetonUniversity/ILAng)
  * Princeton modeling and Verification Platform for SoCs using ILAs
* [autosva](https://github.com/PrincetonUniversity/AutoSVA)
  * Generates FV testbenches and SVA properties based on interface annotations + GPT4
* [autocc](https://github.com/morenes/AutoCC)
  * Frontend for JG/SBY to automatically discover covert channels in time-shared hardware
* [pono](https://github.com/upscale-project/pono)
  * Extensible SMT-based model checker implemented in C++.
* [sby](https://github.com/YosysHQ/sby)
  * Front-end for Yosys-based formal verification flows.
* [z3](https://github.com/Z3Prover/z3)
  * Microsoft research theorem prover

## Linters
* [svlint](https://github.com/dalance/svlint)
  * SystemVerilog linter
* [svlint-action](https://github.com/dalance/svlint-action)
  * GitHub action for svlint
* [verible](https://github.com/chipsalliance/verible)
  * SystemVerilog developer tools, including a parser, style-linter, and formatter
* [verilator](https://github.com/verilator/verilator)
  * SystemVerilog simulator and lint system

## Register Design
* [gen_registers](https://github.com/lsteveol/gen_registers)
  * Python based tool for generating hardware registers and their associated files
* [hdl-registers](https://github.com/hdl-registers/hdl-registers)
  * Fast HDL register code generator
* [rggen](https://github.com/rggen/rggen)
  * Configuration and status register generator
* [open-register-design-tool](https://github.com/Juniper/open-register-design-tool)
  * Generate register RTL, models, and docs using SystemRDL or JSpec input
* [peakrdl](https://github.com/SystemRDL/PeakRDL)
  * SystemRDL based control & status register (CSR) toolchain
* [systemrdl](https://github.com/SystemRDL/systemrdl-compiler)
  * Generic compiler front-end for SystemRDL 2.0 register description language

## Schematics
* [d3-hwschematics](https://github.com/Nic30/d3-hwschematic)
  * Schematic visualizer
* [kaktus2dev](https://github.com/kactus2/kactus2dev)
  * Graphical EDA tool based on the IP-XACT standard
* [openplc_editor](https://github.com/thiagoralves/OpenPLC_Editor)
  * IDE capable of creating programs for the OpenPLC Runtime
* [oregano](https://github.com/drahnr/oregano)
  * Schematic capture and circuit simulator
* [qucs_s](https://github.com/ra3xdh/qucs_s)
  * Integrated circuit simulator with Graphical User Interface
* [hdl21schematics](https://github.com/Vlsir/Hdl21Schematics)
  * Hdl21 Schematics
* [xschem](https://github.com/StefanSchippers/xschem)
  * Schematic editor for VLSI/Asic/Analog custom designs

## Electronics Simulators
* [champsim](https://github.com/ChampSim/ChampSim)
  * Trace-based simulator for a microarchitecture study
* [dromajo](https://github.com/chipsalliance/dromajo)
  * RISC-V RV64GC functional emulator
* [eesim](https://github.com/danchitnis/EEsim)
  * Browser-based SPICE circuit simulator
* [essent](https://github.com/ucsc-vama/essent)
  * High-performance FIRRTL (Chisel) simulator
* [firesim](https://github.com/firesim/firesim)
  * FPGA-accelerated Cycle-accurate Hardware Simulation in the Cloud
* [gem5](https://github.com/gem5/gem5)
  * Modular simulator platform for computer-system architecture research
* [muchisim](https://github.com/PrincetonUniversity/muchisim)
  * Cycle-level simulator for PPA analysis of distributed multi-chiplet designs.
* [ghdl](https://github.com/ghdl/ghdl)
  * VHDL 2008/93/87 simulator
* [icarus](https://github.com/steveicarus/iverilog.git)
  * Verilog IEEE-1364 simulator
* [irsim](https://github.com/RTimothyEdwards/irsim)
  * Switch-level simulator for digital circuits
* [libsystemctlm-soc](https://github.com/Xilinx/libsystemctlm-soc)
  * SystemC/TLM-2.0 Co-simulation framework
* [logisim-evolution](https://github.com/logisim-evolution/logisim-evolution)
  * Digital logic design tool and simulator
* [lwtr4sc](https://github.com/Minres/LWTR4SC)
  * Transaction recording for SystemC
* [ngspice](http://ngspice.sourceforge.net/)
  * Spice simulator
* [noxim](https://github.com/davidepatti/noxim)
  * Network on Chip Simulator
* [nvc](https://github.com/nickg/nvc)
  * VHDL compiler and simulator
* [pysysc](https://github.com/accellera-official/PySysC)
  * Python package to make SystemC usable from Python
* [qemu](https://github.com/qemu/qemu)
  * Generic and open source machine & userspace emulator and virtualizer
* [ramulator2](https://github.com/CMU-SAFARI/ramulator2)
  * Cycle accurate DRAM simulator
* [renode](https://github.com/renode/renode)
  * Generic and open source machine emulator
* [sax](https://github.com/flaport/sax)
  * S-parameter based frequency domain circuit simulation
* [SimEng](https://github.com/UoB-HPC/SimEng)
  * Fast, easily modifiable, cycle-level CPU simulator framework
* [simulide](https://github.com/SimulIDE/SimulIDE)
  * SimulIDE is a simple real-time electronic circuit simulator
* [SST](https://github.com/sstsimulator/sst-core)
  * Simulation platform to connect multiple simulated hardware objects
* [systemc-components](https://github.com/Minres/SystemC-Components)
  * SystemC simulation productivity library
* [tiny-five](https://github.com/OpenMachine-ai/tinyfive)
  * Lightweight RISC-V emulator and assembler written entirely in Python
* [xictools](https://github.com/wrcad/xictools)
  * Circuit simulation package
* [xyce](https://github.com/Xyce/Xyce)
  * Parallel spice simulator from Sandia national labs
* [verilator](https://github.com/verilator/verilator)
  * SystemVerilog simulator and lint system

## Verification Frameworks
* [adc-eval](https://github.com/esynr3z/adc-eval)
  * Python tools for ADC performance analysis
* [awsteria_infra](https://github.com/bluespec/AWSteria_Infra)
  * Middleware for AWS hosted FPGA applications
* [anasysmod](https://github.com/sgherbst/anasymod)
  * Framework for FPGA emulation of mixed-signal systems
* [cocotb](https://github.com/cocotb/cocotb)
  * Python based cosimulation library for VHDL and Verilog testbenches
* [cocotbext-axi](https://github.com/alexforencich/cocotbext-axi)
  * AXI interface modules for Cocotb
* [cocotbext-pcie](https://github.com/alexforencich/cocotbext-pcie)
  * PCI express simulation framework for Cocotb
* [constrainedrandom](https://github.com/imaginationtech/constrainedrandom)
  * Python package for creating and solving constrained randomization problems
* [cvc](https://github.com/d-m-bailey/cvc)
  * CVC: Circuit Validity Checker
* [core-v-verif](https://github.com/openhwgroup/core-v-verif)
  * Functional verification project for the CORE-V family of RISC-V cores
* [ddr5_phy](https://github.com/Shehab-Naga/ddr5_phy)
  * UVM testbench for DDR5 PHY
* [fault](https://github.com/leonardt/fault)
  * Python package for testing hardware
* [force-riscv](https://github.com/openhwgroup/force-riscv)
  * Instruction Set Generator for RISC-V
* [frame](https://github.com/maestro-project/frame)
  * Fast Roofline Analytical Modeling and Estimation
* [fstdumper](https://github.com/semify-eda/fstdumper)
  * Verilog VPI module to dump FST (Fast Signal Trace) databases
* [lctime](https://codeberg.org/librecell/lctime)
  * Library cell characterization
* [maestro](https://github.com/maestro-project/maestro)
  * Analytical cost model evaluating DNN mappings (dataflows and tiling)
* [msdsl](https://github.com/sgherbst/msdsl)
  * Automatic generation of real number models from analog circuits
* [netgen](https://github.com/RTimothyEdwards/netgen)
  * LVS tool for comparing SPICE or verilog netlists
* [openplc_v3](https://github.com/thiagoralves/OpenPLC_v3)
  * OpenPLC Runtime version 3
* [opensta](https://github.com/The-OpenROAD-Project/OpenSTA)
  * Signoff quality STA engine used by OpenRoad
* [opentimer](https://github.com/OpenTimer/OpenTimer)
  * High performance static timing analysis
* [openvaf](https://github.com/pascalkuthe/OpenVAF)
  * Next generation Verilog-A compiler
* [osvvm](https://github.com/OSVVM/OsvvmLibraries)
  * A VHDL verification framework
* [pcievhost](https://github.com/wyvernSemi/pcievhost)
  * PCIe (1.0a to 2.0) Virtual host model for verilog
* [pyspice](https://github.com/PySpice-org/PySpice)
  * Python interface for ngspice and xyce
* [pyucis](https://github.com/fvutils/pyucis)
  * Python API to Unified Coverage Interoperability Standard (UCIS) Data
* [pyuvm](https://github.com/pyuvm/pyuvm)
  * SystemVerilog UVM written in Python
* [pyvsc](https://github.com/fvutils/pyvsc)
  * Python packages for SystemVerilog UVM style Verification Stimulus and Coverage
* [raft](https://github.com/Xilinx/RAFT)
  * Rapid Abstraction FPGA Toolbox
* [riscv-dv](https://github.com/chipsalliance/riscv-dv)
  * Random instruction generator for RISC-V processor verification
* [rohd-cosim](https://github.com/intel/rohd-cosim)
  * Framework for cosimulation between the ROHD and SystemVerilog simulators.
* [rohd-vf](https://github.com/intel/rohd-vf)
  * ROHD-based verification and testbench framework in Dart.
* [switchboard](https://github.com/zeroasiccorp/switchboard/)
  * Communication framework for RTL simulation and emulation
* [svreal](https://github.com/sgherbst/svreal)
  * Synthesizable real number library in SystemVerilog (fixed & floating point formats)
* [systemctlm-cosim-demo](https://github.com/Xilinx/systemctlm-cosim-demo)
  * Demo system for libsystemctlm-soc library
* [sv_waveterm](https://github.com/PeterMonsson/sv_waveterm)
  * Generate text waves in simulation log file
* [uvvm](https://github.com/UVVM/UVVM)
  * Library for making very structured VHDL-based testbenches.
* [v2k-top](https://github.com/kev-cam/v2k-top)
  * Parser/simulation framework for Verilog & C++
* [vidbo](https://github.com/olofk/vidbo)
  * Virtual development board
* [vunit](https://github.com/VUnit/vunit)
  * Unit testing framework for VHDL/SystemVerilog

## Physics
* [devsim](https://github.com/devsim)
  * TCAD Semiconductor Device Simulator
* [elmer](https://github.com/ElmerCSC/elmerfem)
  * Finite Element Solver
* [femwell](https://github.com/HelgeGehring/femwell)
  * Finite element based simulation tool for integrated circuits, electric and photonic
* [hotspot](https://github.com/uvahotspot/HotSpot)
  * Thermal modeling tool for use in architectural studies
* [meep](https://github.com/NanoComp/meep)
  * Finite-difference-time-domain (FDTD) electromagneic simulation
* [paraview](https://github.com/Kitware/ParaView)
  * Data Analysis and Visualization Application
* [pact](https://github.com/peaclab/PACT)
  * Thermal simulator
* [scikit-rf](https://github.com/scikit-rf/scikit-rf)
  * RF and Microwave Engineering Scikit

## Waveform Viewers
* [scviewer](https://github.com/Minres/SCViewer)
  * Eclipse plugins to display VCD (e.g. created by SystemC VCD trace).
* [d3wave](https://github.com/Nic30/d3-wave)
  * D3.js based wave (signal) visualizer
* [gtkwave](https://github.com/gtkwave/gtkwave)
  * GTK+ based VCD waveform viewer
* [iio-oscilloscope](https://github.com/analogdevicesinc/iio-oscilloscope)
  * GTK+ based oscilloscope application for interfacing with various IIO devices
* [konata](https://github.com/shioyadan/Konata)
  * Instruction pipeline visualizer for Gem5
* [npTDMS](https://github.com/adamreeve/npTDMS)
  * Python module for reading TDMS files produced by LabView
* [scopy](https://github.com/analogdevicesinc/scopy)
  * Software oscilloscope and signal analysis toolset
* [sigrok](https://github.com/sigrokproject)
  * Portable, signal analysis software suite (logic analyzers, scopes, multimeters, and more)
* [simview](https://github.com/pieter3d/simview)
  * Text-based SystemVerilog design browser and waveform viewer
* [sootty](https://github.com/Ben1152000/sootty)
  * Command-line tool for displaying vcd waveforms
* [spyci](https://github.com/gmagno/spyci)
  * Python package to parse spice raw data files
* [verilog-vcd-parser](https://github.com/ben-marshall/verilog-vcd-parser)
  * Parser for Value Change Dump (VCD) files
* [wavebin](https://github.com/sam210723/wavebin)
  * Oscilloscope waveform capture viewer and converter
* [waveforms-live](https://github.com/Digilent/waveforms-live)
  * Browser based analog waveform viewer

# Designs & Generators

## Accelerators
* [aes](https://github.com/secworks/aes)
  * Symmetric block cipher AES (Advanced Encryption Standard)
* [ara](https://github.com/pulp-platform/ara)
  * Vector Unit, compatible with the RISC-V Vector Extension
* [bfg](https://github.com/growly/bfg)
  * Compiler for Reduced-Complexity Reconfigurable Fabrics
* [bismp](https://github.com/EECS-NTNU/bismo/)
  * Chisel-based bit-serial matrix multiplication accelerator generator
* [finn](https://github.com/Xilinx/finn)
  * Quantized NN to FPGA dataflow accelerator generator
* [fftgenerator](https://github.com/ucb-bar/FFTGenerator)
  * MMIO-Based FFT Generator
* [fpu](https://github.com/dawsonjon/fpu)
  * Synthesizable ieee 754 floating point library in verilog
* [garnet](https://github.com/StanfordAHA/garnet)
  * CGRA generator
* [gemmini](https://github.com/ucb-bar/gemmini)
  * Berkeley Spatial Array Generator
* [gplgpu](https://github.com/asicguy/gplgpu)
  * GPL v3 2D/3D graphics engine in verilog
* [core_jpeg](https://github.com/ultraembedded/core_jpeg)
  * High throughput JPEG decoder in Verilog for FPGA
* [fftgenerator](https://github.com/ucb-bar/FFTGenerator)
  * Chisel based FFT generator
* [h265-encoder-rtl](https://github.com/openasic-org/h265-encoder-rtl)
  * H.265 Video Encoder IP Core
* [logicnets](https://github.com/Xilinx/logicnets)
  * Train and generate LUT-based neural networks
* [nngen](https://github.com/NNgen/nngen)
  * Fully-Customizable Hardware Synthesis Compiler for Deep Neural Network
* [nvdla](https://github.com/nvdla/hw)
  * NVIDIA Deep Learning Accelerator (NVDLA)
* [nyuziprocessor](https://github.com/jbush001/NyuziProcessor)
  * GPGPU microprocessor architecture
* [opencgra](https://github.com/pnnl/OpenCGRA)
  * Parametrizable Coarse-Grained Reconfigurable Array (CGRA) Generator
* [openofdm](https://github.com/jhshi/openofdm)
  * 802.11 OFDM PHY decoder
* [openspike](https://github.com/sfmth/OpenSpike)
  * Spiking neural network accelerator
* [project-zipline](https://github.com/opencomputeproject/Project-Zipline)
  * Zipline lossless compression implementation
* [pyfda](https://github.com/chipmuenk/pyFDA)
  * Python Filter Design Analysis Tool
* [ranc](https://github.com/UA-RCL/RANC)
  * Reconfigurable architecture for neuromorphic computing
* [sha256](https://github.com/secworks/sha256)
  * SHA-256 hash function (NIST FIPS 180-4)
* [sha512](https://github.com/secworks/sha512)
  * SHA-512 hash function (NIST FIPS 180-4)
* [sha3](https://github.com/ucb-bar/sha3)
  * Berkeley SHAR3 ROCC Accelerator
* [serpens](https://github.com/linghaosong/Serpens)
  * HBM FPGA based SpMV Accelerator
* [sextans](https://github.com/linghaosong/Sextans)
  * FPGA accelerator for Sparse-Matrix Dense-Matrix Multiplication (SpMM)
* [spiral](https://github.com/spiral-software/spiral-software)
  * Spiral based FFT generator
* [tvm-vta](https://github.com/apache/tvm-vta)
  * Opwn, modular, deep learning accelerator
* [verigood-ml](https://github.com/VeriGOOD-ML/public)
  * Verilog Generator, Optimized for Designs for Machine Learning
* [Viterbi](https://github.com/Archit-halder/Viterbi-Algorithm)
  * Viterbi encoder/decoder (2,1,4)
* [Viterbi](https://github.com/jfoshea/Viterbi-Decoder-in-Verilog)
  * Viterbi decoder (2,1,3) (3,2,2) (2,1,3) (3,2,2)
* [verigpu](https://github.com/hughperkins/VeriGPU)
  * OpenSource GPU, loosely based on RISC-V ISA
* [verilog-lfsr](https://github.com/alexforencich/verilog-lfsr)
  * Parametrizable combinatorial parallel LFSR/CRC module
* [vortex](https://github.com/vortexgpgpu/vortex)
  * Full-system RISCV-based GPGPU processor

## AIB
* [aib](https://github.com/chipsalliance/aib-phy-hardware)
  * Advanced Interface Bus (AIB) die to die hardware
* [aib-protocols](https://github.com/chipsalliance/aib-protocols)
  * Advanced Interface Bus (AIB) Protocol IP
* [axi4_aib_bridge](https://github.com/lmco/axi4_aib_bridge)
  * AXI4/AIB Bridge RTL

## AXI
* [axi](https://github.com/pulp-platform/axi)
  * (Pulp) AXI SystemVerilog synthesizable IP
* [axi-crossbar](https://github.com/dpretet/axi-crossbar)
  * AXI4 crossbar implemented in SystemVerilog
* [cocotbext-axi](https://github.com/alexforencich/cocotbext-axi)
  * AXI interface modules for Cocotb
* [tvip-apb](https://github.com/taichi-ishitani/tvip-apb)
  * UVM based AMBA APB VIP
* [tvip-axi](https://github.com/taichi-ishitani/tvip-axi)
  * UVM based AMBA AXI VIP
* [verilog-axis](https://github.com/alexforencich/verilog-axis)
  * (Forencich) Verilog AXI stream components for FPGA implementation
* [wb2axip](https://github.com/ZipCPU/wb2axip)
  * AXI-Wishbone bus bridges

## Analog Circuits
* [ams_kgd](https://github.com/USCPOSH/AMS_KGD)
  * Repository for Known Good Analog Designs (KGDs)
* [analog_blocks](https://github.com/mabrains/Analog_blocks)
  * Basic building blocks (OTA, BandGap and LDO) in Skywater 130nm.
* [openfasoc](https://github.com/idea-fasoc/OpenFASOC)
  * Automated Mixed Signal SoC Synthesis Framework
* [open-pmic](https://github.com/westonb/open-pmic)
  * Current mode buck converter on the SKY130 PDK

## Chip Packaging
* [bsg_packaging](https://github.com/bespoke-silicon-group/bsg_packaging)
  * Open-Source Hardware Accelerator Packages and Sockets

## Boards
* [bsg_motherboards](https://github.com/bespoke-silicon-group/bsg_motherboards)
  * BaseJump Hardware Accelerator Motherboards
* [gmm7550](https://github.com/ak-fau/gmm7550)
  * CologneChip GateMate FPGA Module: GMM-7550
* [google-coral-baseboard](https://github.com/antmicro/google-coral-baseboard)
  * Open hardware baseboard for the Google Coral i.MX8 + Edge TPU SoM
* [hardware-components](https://github.com/antmicro/hardware-components)
  * Collection of KiCad components
* [parallella-hw](https://github.com/parallella/parallella-hw)
  * Collection of open source boards from Adapteva

## Connectivity
* [bsg_ddr3_io](https://github.com/bespoke-silicon-group/bsg_ddr3_io)
  * BaseJump DDR3 I/O Design
* [core_ddr3_controller](https://github.com/ultraembedded/core_ddr3_controller)
  * DDR3 memory controller in Verilog for various FPGAs
* [ctucanfd_ip_core](https://gitlab.fel.cvut.cz/canbus/ctucanfd_ip_core)
  * CAN with Flexible Data-rate
* [hdmi](https://github.com/hdl-util/hdmi)
  * Send video/audio over HDMI on an FPGA
* [i2c](https://github.com/hdl-util/i2c)
  * Fully featured implementation of Inter-IC (I2C) bus master
* [idma](https://github.com/pulp-platform/iDMA)
  * Modular, parametrizable, and highly flexible Data Movement Accelerator
* [io-gen](https://github.com/GT-CHIPS/IO-Gen)
  * IO cell generator
* [litedram](https://github.com/enjoy-digital/litedram)
  * Small footprint and configurable DRAM (litex)
* [liteeth](https://github.com/enjoy-digital/liteeth)
  * Small footprint and configurable Ethernet core
* [litescope](https://github.com/enjoy-digital/litescope)
  * Small footprint and configurable embedded FPGA logic analyzer
* [litepice](https://github.com/enjoy-digital/litepcie)
  * Small footprint and configurable PCIe core
* [nocrouter](https://github.com/agalimberti/NoCRouter)
  * Network-on-Chip Router
* [omi_device_ice](https://github.eom/OpenCAPI/omi_device_ice)
  * Open memory interface example device
* [opencapi_accel](https://github.com/OpenCAPI/oc-accel)
  * OpenCAPI acceleration framework
* [opencapi_client](https://github.com/OpenCAPI/OpenCAPI3.0_Client_RefDesign)
  * OpenCAPI client reference design
* [openserdes](https://github.com/SparcLab/OpenSERDES)
  * Digitally synthesizable architecture for SerDes using Skywater130
* [pymtl3-net](https://github.com/cornell-brg/pymtl3-net)
  * Cornell parameterizable OCN (on-chip network) generator
* [ravenoc](https://github.com/aignacio/ravenoc)
  * Configurable HDL NoC (Network-On-Chip)
* [tnoc](https://github.com/taichi-ishitani/tnoc)
  * Network on Chip Implementation written in SytemVerilog
* [usb3_camera](https://github.com/circuitvalley/USB_C_Industrial_Camera_FPGA_USB3)
  * USB C Industrial Camera Project
* [usb_cdc](https://github.com/ulixxe/usb_cdc/)
  * Minimal USB CDC (ACM) implementation in verilog
* [usb_dfu](https://github.com/ulixxe/usb_dfu/tree/main)
  * Verilog implementation of the USB Device Class Specification
* [umi](https://github.com/zeroasiccorp/umi)
  * Universal Memory Interface
* [verilog-ethernet](https://github.com/alexforencich/verilog-ethernet)
  * Verilog Ethernet components for FPGA implementation
* [verilog-i2c](https://github.com/alexforencich/verilog-i2c)
  * Verilog I2C interface for FPGA implementation
* [verilog-uart](https://github.com/alexforencich/verilog-uart)
  * Verilog UART
* [verilog-pcie](https://github.com/alexforencich/verilog-pcie)
  * Verilog PCI express components
* [verilog-wishbone](https://github.com/alexforencich/verilog-wishbone)
  * Verilog wishbone components
* [vis4mesh](https://github.com/ueqri/vis4mesh)
  * Visualization tool for designing mesh Network-on-Chips
* [vivado-library](https://github.com/Digilent/vivado-library)
  * IP cores and interface definitions compatible with Xilinx Vivado IP Catalog
* [wav-d2d-hw](https://github.com/waviousllc/wav-d2d-hw)
  * 8lane Wlink with D2D and a single AXI Target/Initiator
* [wav-lpddr-hw](https://github.com/waviousllc/wav-lpddr-hw)
  * DDR (WDDR) Physical interface (PHY) Hardware
* [wav-slink-hw](https://github.com/waviousllc/wav-slink-hw)
  * Chiplet link
* [wav-wlink-hw](https://github.com/waviousllc/wav-wlink-hw)
  * Chiplet link

## CPUs
* [a2i](https://github.com/openpower-cores/a2i)
  * A2I POWER processor core RTL (VHDL)
* [ara](https://github.com/pulp-platform/ara)
  * 64-bit Vector unit coprocessor to Ccva6
* [black-parrot](https://github.com/black-parrot/black-parrot)
  * Linux-capable RISC-V multicore
* [cfu-playground](https://github.com/google/CFU-Playground/)
  * Famework for playing with custom opcodes to accelerate TensorFlow Lite for Microcontrollers
* [cores-swerv](https://github.com/chipsalliance/Cores-SweRV)
  * SweRV EH1 RISC-Vcore
* [cores-swerv-el2](https://github.com/chipsalliance/Cores-SweRV-EL2)
  * SweRV EL2 RISC-V Core
* [core-v-verif](https://github.com/openhwgroup/core-v-verif)
  * Functional verification project for the CORE-V family of RISC-V cores
* [cva6](https://github.com/openhwgroup/cva6)
  * Linux capable RISC-V CPU
* [cve2](https://github.com/openhwgroup/cve2)
  * Small two-stage 32 bit RISC-V CPU core (RV32IMC/EMC)
* [cv32e40s](https://github.com/openhwgroup/cv32e40s)
  * RV32IMFCX RISC-V 4-stage secure RISC-V CPU
* [cv32e40x](https://github.com/openhwgroup/cv32e40x)
  * RV32IMFCX RISC-V 4-stage compute RISC-V CPU
* [cvw](https://github.com/openhwgroup/cvw)
  * Configurable RISC-V Processor for RISC-V System-on-Chip Design textbook.
* [ibex](https://github.com/lowRISC/ibex)
  * Small 32 bit RISC-V CPU core
* [lizard](https://github.com/cornell-brg/lizard)
  * Cornell modular RV64IM Out-of-Order Processor Built with PyMTL
* [microwatt](https://github.com/antonblanchard/microwatt)
  * Open POWER ISA softcore written in VHDL 2008
* [minimax](https://github.com/gsmecher/minimax)
  * A Compressed-First, Microcoded RISC-V CPU
* [muntjac](https://github.com/lowRISC/muntjac)
  * Simple 64-bit RISC-V multicore processor
* [neorv32](https://github.com/stnolting/neorv32)
  * Customizable and highly extensible MCU-class 32-bit RISC-V (VHDL)
* [openxiangshan](https://github.com/OpenXiangShan/XiangShan)
  * Open-source high-performance RISC-V processor
* [picorv32](https://github.com/YosysHQ/picorv32)
  * Size-Optimized RISC-V CPU
* [rocket-chip](https://github.com/chipsalliance/rocket-chip)
  * Linux capable RISC-V Rocket Chip Generator
* [rioschip](https://github.com/b224hisl/rioschip)
  * Out of order RISC-V core
* [serv](https://github.com/olofk/serv)
  * SErial RISC-V CPU
* [snitch](https://github.com/pulp-platform/snitch)
  * Lean but mean RISC-V system
* [veer](https://github.com/chipsalliance/Cores-VeeR-EL2)
  * 32-bit integer machine-mode RISC-V CPU
* [vroom](https://github.com/MoonbaseOtago/vroom)
  * High performance RISC-V CPU

## FPGA Architectures
* [fabulous](https://github.com/FPGA-Research-Manchester/FABulous)
  * Fabric generator and CAD tools
* [fabric_team](https://github.com/ucb-cs250/fabric_team)
  * Simple Berkeley FPGA generator class project
* [openfpga](https://github.com/lnis-uofu/OpenFPGA)
  * FPGA IP Generator
* [prga](https://github.com/PrincetonUniversity/prga)
  * Open-source FPGA research and prototyping framework

## Libraries
* [async_fifo](https://github.com/dpretet/async_fifo)
  * Dual clock asynchronous FIFO
* [basejump_stl](https://github.com/bespoke-silicon-group/basejump_stl)
  * Library of SystemVerilog components
* [basic_verilog](https://github.com/pConst/basic_verilog)
  * Library of SystemVerilog components
* [berkeley-hardfloat](https://github.com/ucb-bar/berkeley-hardfloat)
  * Berkeley hardware floating point units
* [common_cells](https://github.com/pulp-platform/common_cells)
  * Library of SystemVerilog components
* [cvfpu](https://github.com/openhwgroup/cvfpu)
  * Parametric floating-point unit
* [hdl](https://github.com/analogdevicesinc/hdl)
  * Library of Analog Deveices specific components
* [lambdalib](https://github.com/siliconcompiler/lambdalib)
  * Hardware abstraction library
* [lambdapdk](https://github.com/siliconcompiler/lambdapdk)
  * Library of open source Process Design Kits (PDKs)
* [libsv](https://github.com/bensampson5/libsv)
  * Parameterized SystemVerilog digital hardware library
* [mathlib](https://github.com/asfigo/mathlib)
  * SystemVerilog MathLib
* [oh](https://github.com/aolofsson/oh)
  * Library of Verilog components
* [Open Logic](https://github.com/open-logic/open-logic)
  * Open Logic FPGA Standard Library
* [pztb-core](https://github.com/pezy-computing/pztb-core)
  * Collection of class libraries for testbench development
* [pzbcm](https://github.com/pezy-computing/pzbcm)
  * Basic common modules
* [rohd-hcl](https://github.com/intel/rohd-hcl)
  * Library of reusable & configurable hardware components developed with ROHD
* [surf](https://github.com/slaclab/surf)
  * Giant VHDL library for FPGA development
* [vlsiffra](https://github.com/antonblanchard/vlsiffra)
  * Fast and efficient standard cell based adders and multipliers

## Memory
* [core_axi_cache](https://github.com/ultraembedded/core_axi_cache)
  * 128KB AXI cache (32-bit in, 256-bit out)
* [cv-hpdcache](https://github.com/openhwgroup/cv-hpdcache)
  * High-Performance L1 Dcache
* [bsg_fakeram](https://github.com/bespoke-silicon-group/bsg_fakeram)
  * Fake RAM generator
* [huancun](https://github.com/OpenXiangShan/HuanCun)
  * Open-source high-performance non-blocking cache
* [openram](https://github.com/VLSIDA/OpenRAM)
  * Static random access memory (SRAM) compiler.
* [lake](https://github.com/StanfordAHA/lake)
  * Synthesizable memory generator

## Systems
* [caliptra](https://github.com/chipsalliance/caliptra)
  * Caliptra Root of Trust Architecture
* [caliptra-rtl](https://github.com/chipsalliance/caliptra-rtl)
  * Caliptra Root of Trust (RTL)
* [beagle_sdr_gps](https://github.com/jks-prv/Beagle_SDR_GPS)
  * KiwiSDR: BeagleBone web-accessible GPS/SDR
* [bsg_manycore](https://github.com/bespoke-silicon-group/bsg_manycore)
  * Tile based architecture designed for efficiency & scalability
* [cep](https://github.com/CommonEvaluationPlatform/CEP)
  * RISC-V based Common Evaluation Platform (CEP)
* [esp](https://github.com/sld-columbia/esp)
  * Heterogeneous SoC architecture and IP design platform
* [falcon](https://github.com/falkenber9/falcon)
  * Fast Analysis of LTE Control channels
* [hero](https://github.com/pulp-platform/hero)
  * FPGA-based research platform for heterogeneous design
* [litex](https://github.com/enjoy-digital/litex)
  * SoC builder framework
* [metroboy](https://github.com/aappleby/metroboy)
  * Gate-level simulators and tools for the original Game Boy
* [openfasoc](https://github.com/idea-fasoc/OpenFASOC)
  * Open Source FASOC generators
* [openpiton](https://github.com/PrincetonUniversity/openpiton)
  * General purpose, multithreaded manycore processor
* [opentitan](https://github.com/lowRISC/opentitan)
  * Open source silicon root of trust
* [openwifi-hw](https://github.com/open-sdr/openwifi-hw)
  * IEEE 802.11 WiFi baseband FPGA (chip) design
* [pulp](https://github.com/pulp-platform/pulp)
  * Multicore RISC-V based SoC
* [pulpissimo](https://github.com/pulp-platform/pulpissimo)
  * Single core RISC-V based SoC
* [rose](https://github.com/ucb-bar/RoSE)
  * Unified simulation platform for robotic systems
* [senseq](https://github.com/EMIL-YORKU/SensSeq)
  * Mixed-signal system on chip for nanopore-based DNA sequencing
* [verilogboy](https://github.com/zephray/VerilogBoy)
  * Game Boy compatible machine with Verilog
* [wulpus](https://github.com/pulp-bio/wulpus)
  * Wearable low-power ultrasound probe
* [x-heep](https://github.com/esl-epfl/x-heep)
  * Extendable and configurable RISC-V SoC

## Boards

* [artix-dc-scm](https://github.com/antmicro/artix-dc-scm)
  * Antmicro OCP data center secure control module
* [arty-mpw-tester](https://github.com/antmicro/arty-mpw-tester)
  * Antmicro Caravel fanout board
* [fomu](https://github.com/im-tomu/fomu-hardware)
  * Tiny USB FPGA board
* [icebreaker](https://github.com/icebreaker-fpga/icebreaker)
  * Low cost FPGA development board
* [lpddr5-testbed](https://github.com/antmicro/lpddr5-testbed)
  * Antmicro lpddr5 testbed
* [PicoEVB](https://github.com/RHSResearchLLC/PicoEVB)
  * M.2 80mm Artix FPGA evaluation board
* [qomu-dev-board](https://github.com/QuickLogic-Corp/qomu-dev-board)
  * Quicklogic efpga USB dev board
* [scalenode-cm4-baseboard](https://github.com/antmicro/scalenode-cm4-baseboard)
  * Antmicro basedboard for RPI CM4
* [sodimm-ddr5-tester](https://github.com/antmicro/sodimm-ddr5-tester)
  * Antmicro ddr5 tester board

# Education

## Analog Design

* [book-on-mos-stagse](https://github.com/bmurmann/Book-on-MOS-stages)
  * Analysis and Design of Elementary MOS Amplifier Stages
* [SiliWiz](https://tinytapeout.com/siliwiz/introduction/)
  * Browser based interactive circuit design tool.

## Board Design

## Digital Design

* [cornell-ece4750](https://github.com/cornell-ece4750)
  * ECE 4750 Computer Architecture
* [cornell-ece5745](https://github.com/cornell-ece5745)
  * ECE 5745 Complex Digital ASIC Design
* [stanford-ee272a](https://priyanka-raina.github.io/ee272a-winter2021)
  * EE272A Design Projects in VLSI Systems I
* [stanford-ee272b](https://priyanka-raina.github.io/ee272b-spring2021)
  * EE272B Design Projects in VLSI Systems II

## FPGA Design

----

# Other Awesome Lists

* [ben-marshall](https://github.com/ben-marshall/awesome-open-hardware-verification)
  * Hardware verification
* [computer-engineering-resources](https://github.com/rajesh-s/computer-engineering-resources)
  * A curated list of Computer Engineering/Architecture resources
* [delftopenhardware](https://github.com/delftopenhardware/awesome-open-hardware)
  * Open hardware materials
* [drom](https://github.com/drom/awesome-hdl)
  * HDL languages
* [hdl](https://github.com/hdl/awesome)
  * Hardware description resources
* [kicad-3rd-party-tools](https://github.com/devbisme/kicad-3rd-party-tools)
  * List of 3rd party KiCad software packages
* [mattvenn](https://github.com/mattvenn/awesome-opensource-asic-resources)
  * ASIC resources
* [pkuzjx](https://github.com/pkuzjx/eda-collection)
  * Open source EDA resources
* [semiconduoctor-startups](https://github.com/aolofsson/awesome-semiconductor-startups)
  * Semiconductor startups
* [joamateb](https://github.com/joamatab/awesome_photonics)
  * Photonics
