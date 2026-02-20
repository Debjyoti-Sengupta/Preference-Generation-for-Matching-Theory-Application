# Preference-Generation-for-Matching-Theory-Application
Generates preference lists for two parties (Vehicles and VMs in a RSU) involved in a Matching Game
Vehicles denoted by v and VMs belonging to an RSU (Roadside Unit) denoted by m are considered as two factions involved in a Matching Game, taking inspiration from the Gale-Shapley Algorithm. The preference lists that form the basis of the algorithm are generated using the code.

There are 3 variants: Pref_Gen.py , which generates the preferences based on defined dictionaries of vehicles and VMs with specific parameters. Pref_Gen_excelread.py does the same but with input from a spreadsheet instead of user defined dictionaries.
Offload.py adds an extra step of creating a partition of the computational tasks originating from the vehicles for partially offloading them to VMs after the preference lists are passed through a Matching Algorithm (like Gale-Shapley's).
