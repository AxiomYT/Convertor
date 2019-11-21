#----------//Variables\\----------#

import webbrowser
import math

selector1 = 0;
selector = 0;
unit1 = 0;
unit2 = 0;
ans = 0;
num1 = 0;
input1 = 0;

# Speed of light in air (Speed of light in a vacuum is 300000000 Kilometres per second)
c = 299792458; # Kilometres Per Second

#----------//Functions\\----------#

def length():
    
    unit1 = 0;
    unit2 = 0;
    ans = 0;
    num1 = 0;

    print("We can convert using the units; km, m, cm, mm, um, nm, mi, yd, ft, in, nmi");
    unit1 = input("Which unit would you like to convert from: ");
    unit2 = input("Which unit would you like to convert to: ");
    num1 = input("Enter your value: " );
    lengthcalc(unit1, unit2, num1);

def lengthcalc(unit1, unit2, num1):

#----------//Kilometres\\----------#
    if unit1 == "km" and unit2 == "m":
        ans = float(num1) * 1000;
        
    elif unit1 == "km" and unit2 == "cm":
        ans = float(num1) * 100000;
        
    elif unit1 == "km" and unit2 == "mm":
        ans = float(num1) * (1*(10**6));
        
    elif unit1 == "km" and unit2 == "um":
        ans = float(num1) * (1*(10**9));
        
    elif unit1 == "km" and unit2 == "nm":
        ans = float(num1) * (1*(10**12));
        
    elif unit1 == "km" and unit2 == "mi":
        ans = float(num1) / 1.609;
        
    elif unit1 == "km" and unit2 == "yd":
        ans = float(num1) * 1093.613;
        
    elif unit1 == "km" and unit2 == "ft":
        ans = float(num1) * 3280.84;
        
    elif unit1 == "km" and unit2 == "in":
        ans = float(num1) * 39370.079;
        
    elif unit1 == "km" and unit2 == "nmi":
        ans = float(num1) / 1.852;
        
        
#----------//Metres\\-----------#
    elif unit1 == "m" and unit2 == "km":
        ans = float(num1) / 1000;
        
    elif unit1 == "m" and unit2 == "cm":
        ans = float(num1) * 100;
        
    elif unit1 == "m" and unit2 == "mm":
        ans = float(num1) * 1000;
        
    elif unit1 == "m" and unit2 == "um":
        ans = float(num1) * (1*(10**6));
        
    elif unit1 == "m" and unit2 == "nm":
        ans = float(num1) * (1*(10**9));
        
    elif unit1 == "m" and unit2 == "mi":
        ans = float(num1) / 1609.344;
        
    elif unit1 == "m" and unit2 == "yd":
        ans = float(num1) * 1.094;
        
    elif unit1 == "m" and unit2 == "ft":
        ans = float(num1) * 3.281;
        
    elif unit1 == "m" and unit2 == "in":
        ans = float(num1) * 39.37;
        
    elif unit1 == "m" and unit2 == "nmi":
        ans = float(num1) / 1852;
        
        
#----------//Centimetres\\----------#
    elif unit1 == "cm" and unit2 == "km":
        ans = float(num1) / 100000;
        
    elif unit1 == "cm" and unit2 == "m":
        ans = float(num1) / 100;
        
    elif unit1 == "cm" and unit2 == "mm":
        ans = float(num1) * 10;
        
    elif unit1 == "cm" and unit2 == "um":
        ans = float(num1) * 10000;
        
    elif unit1 == "cm" and unit2 == "nm":
        ans = float(num1) * (1*(10**7));
        
    elif unit1 == "cm" and unit2 == "mi":
        ans = float(num1) / 160934.4;
        
    elif unit1 == "cm" and unit2 == "yd":
        ans = float(num1) / 91.44;
        
    elif unit1 == "cm" and unit2 == "ft":
        ans = float(num1) / 30.48;
        
    elif unit1 == "cm" and unit2 == "in":
        ans = float(num1) / 2.54;
        
    elif unit1 == "cm" and unit2 == "nmi":
        ans = float(num1) / 185200;
        
        
#----------//Millimetres\\----------#
    elif unit1 == "mm" and unit2 == "km":
        ans = float(num1) / (1*(10**6));
    elif unit1 == "mm" and unit2 == "m":
        ans = float(num1) / 1000;
    elif unit1 == "mm" and unit2 == "cm":
        ans = float(num1) / 10;
    elif unit1 == "mm" and unit2 == "um":
        ans = float(num1) * 1000;
    elif unit1 == "mm" and unit2 == "nm":
        ans = float(num1) * (1*(10**6));
    elif unit1 == "mm" and unit2 == "mi":
        ans = float(num1) * (1.609*(10**6));
    elif unit1 == "mm" and unit2 == "yd":
        ans = float(num1) / 914.4;
    elif unit1 == "mm" and unit2 == "ft":
        ans = float(num1) / 304.8;
    elif unit1 == "mm" and unit2 == "in":
        ans = float(num1) / 25.4;
    elif unit1 == "mm" and unit2 == "nmi":
        ans = float(num1) / (1.852*(10**6))
        
#----------//Micrometres\\----------#
    elif unit1 == "um" and unit2 == "km":
        ans = float(num1) / (1*(10**9));
    elif unit1 == "um" and unit2 == "m":
        ans = float(num1) / (1*(10**6));
    elif unit1 == "um" and unit2 == "cm":
        ans = float(num1) / 10000;
    elif unit1 == "um" and unit2 == "mm":
        ans = float(num1) / 1000;
    elif unit1 == "um" and unit2 == "nm":
        ans = float(num1) * 1000;
    elif unit1 == "um" and unit2 == "mi":
        ans = float(num1) / (1.609*(10**9));
    elif unit1 == "um" and unit2 == "yd":
        ans = float(num1) / 914400;
    elif unit1 == "um" and unit2 == "ft":
        ans = float(num1) / 304800;
    elif unit1 == "um" and unit2 == "in":
        ans = float(num1) / 25400;
    elif unit1 == "um" and unit2 == "nmi":
        ans = float(num1) / (1.852*(10**9));
        
#----------//Nanometres\\----------#
    elif unit1 == "nm" and unit2 == "km":
        ans = float(num1) / (1*(10**12));
    elif unit1 == "nm" and unit2 == "m":
        ans = float(num1) / (1*(10**9));
    elif unit1 == "nm" and unit2 == "cm":
        ans = float(num1) / (1*(10**7));
    elif unit1 == "nm" and unit2 == "mm":
        ans = float(num1) / (1*(10**6));
    elif unit1 == "nm" and unit2 == "um":
        ans = float(num1) / 1000;
    elif unit1 == "nm" and unit2 == "mi":
        ans = float(num1) / (1.609*(10**12));
    elif unit1 == "nm" and unit2 == "yd":
        ans = float(num1) / (9.144*(10**8));
    elif unit1 == "nm" and unit2 == "ft":
        ans = float(num1) / (3.048*(10**8));
    elif unit1 == "nm" and unit2 == "in":
        ans = float(num1) / (2.54*(10**7));
    elif unit1 == "nm" and unit2 == "nmi":
        ans = float(num1) / (1.852*(10**12));

#----------//Miles\\----------#
    elif unit1 == "mi" and unit2 == "km":
        ans = float(num1) * 1.609;
    elif unit1 == "mi" and unit2 == "m":
        ans = float(num1) * 1609.344;
    elif unit1 == "mi" and unit2 == "cm":
        ans = float(num1) * 160934.4;
    elif unit1 == "mi" and unit2 == "mm":
        ans = float(num1) * (1.609*(10**6));
    elif unit1 == "mi" and unit2 == "nm":
        ans = float(num1) * (1.609*(10**12));
    elif unit1 == "mi" and unit2 == "um":
        ans = float(num1) * (1.609*(10**9));
    elif unit1 == "mi" and unit2 == "yd":
        ans = float(num1) * 1760;
    elif unit1 == "mi" and unit2 == "ft":
        ans = float(num1) * 5280;
    elif unit1 == "mi" and unit2 == "in":
        ans = float(num1) * 63360;
    elif unit1 == "mi" and unit2 == "nmi":
        ans = float(num1) / 1.151;

#----------//Yards\\----------#
    elif unit1 == "yd" and unit2 == "km":
        ans = float(num1) / 1093.613;
    elif unit1 == "yd" and unit2 == "m":
        ans = float(num1) / 1.094;
    elif unit1 == "yd" and unit2 == "cm":
        ans = float(num1) * 91.44;
    elif unit1 == "yd" and unit2 == "mm":
        ans = float(num1) * 914.4;
    elif unit1 == "yd" and unit2 == "nm":
        ans = float(num1) * (9.144*(10**8));
    elif unit1 == "yd" and unit2 == "um":
        ans = float(num1) * 914400;
    elif unit1 == "yd" and unit2 == "ft":
        ans = float(num1) * 3;
    elif unit1 == "yd" and unit2 == "in":
        ans = float(num1) * 36;
    elif unit1 == "yd" and unit2 == "nmi":
        ans = float(num1) / 2025.372;
    elif unit1 == "yd" and unit2 == "mi":
        ans = float(num1) / 1760;

#----------//Feet\\----------#
    elif unit1 == "ft" and unit2 == "km":
        ans = float(num1) * 3280.84;
    elif unit1 == "ft" and unit2 == "m":
        ans = float(num1) / 3.281;
    elif unit1 == "ft" and unit2 == "cm":
        ans = float(num1) * 30.48;
    elif unit1 == "ft" and unit2 == "mm":
        ans = float(num1) * 304.8;
    elif unit1 == "ft" and unit2 == "nm":
        ans = float(num1) * (3.048*(10**8));
    elif unit1 == "ft" and unit2 == "um":
        ans = float(num1) * 304800;
    elif unit1 == "ft" and unit2 == "yd":
        ans = float(num1) / 3;
    elif unit1 == "ft" and unit2 == "in":
        ans = float(num1) * 12;
    elif unit1 == "ft" and unit2 == "nmi":
        ans = float(num1) / 6076.115;
    elif unit1 == "ft" and unit2 == "mi":
        ans = float(num1) / 5280;

#----------//Inches\\----------#
    elif unit1 == "in" and unit2 == "km":
        ans = float(num1) / 39370.079;
    elif unit1 == "in" and unit2 == "m":
        ans = float(num1) / 39.37;
    elif unit1 == "in" and unit2 == "cm":
        ans = float(num1) * 2.54;
    elif unit1 == "in" and unit2 == "mm":
        ans = float(num1) * 25.4;
    elif unit1 == "in" and unit2 == "nm":
        ans = float(num1) * (2.54*(10**7));
    elif unit1 == "in" and unit2 == "um":
        ans = float(num1) * 25400;
    elif unit1 == "in" and unit2 == "yd":
        ans = float(num1) / 36;
    elif unit1 == "in" and unit2 == "ft":
        ans = float(num1) / 12;
    elif unit1 == "in" and unit2 == "nmi":
        ans = float(num1) / 72913.386;
    elif unit1 == "in" and unit2 == "mi":
        ans = float(num1) / 63360;

#----------//Nautical Miles\\----------#
    elif unit1 == "nmi" and unit2 == "km":
        ans = float(num1) * 1.852;
    elif unit1 == "nmi" and unit2 == "m":
        ans = float(num1) * 1852;
    elif unit1 == "nmi" and unit2 == "cm":
        ans = float(num1) * 185200;
    elif unit1 == "nmi" and unit2 == "mm":
        ans = float(num1) * (1.852*(10**6));
    elif unit1 == "nmi" and unit2 == "nm":
        ans = float(num1) * (1.852*(10**12));
    elif unit1 == "nmi" and unit2 == "um":
        ans = float(num1) * (1.852*(10**9));
    elif unit1 == "nmi" and unit2 == "yd":
        ans = float(num1) * 2025.372;
    elif unit1 == "nmi" and unit2 == "in":
        ans = float(num1) * 72913.386;
    elif unit1 == "nmi" and unit2 == "ft":
        ans = float(num1) * 6076.115;
    elif unit1 == "nmi" and unit2 == "mi":
        ans = float(num1) * 1.151;

#----------//Input Validation\\----------#
    elif unit1 == unit2: 
        ans = num1;
        
#----------//Suffixes\\----------#
    if unit2 == "km":
      print(str(ans) + " Kilometres\n");
    elif unit2 == "m":
      print(str(ans) + " Miles\n");
    elif unit2 == "cm":
      print(str(ans) + " Centimetres\n");
    elif unit2 == "mm":
      print(str(ans) + " Millimetres\n");
    elif unit2 == "um":
      print(str(ans) + " Micrometres\n");
    elif unit2 == "nm":
      print(str(ans) + " Nanometres\n");
    elif unit2 == "mi":
      print(str(ans) + " Miles\n");
    elif unit2 == "yd":
      print(str(ans) + " Yards\n");
    elif unit2 == "ft":
      print(str(ans) + " Feet\n");
    elif unit2 == "in":
      print(str(ans) + " Inches\n");
    elif unit2 == "nmi":
      print(str(ans) + " Nautical Miles\n");

def weight():
    
    unit1 = 0;
    unit2 = 0;
    ans = 0;
    num1 = 0;

    print("We can convert these weights; lbs, tn, g, kg, ug, mg, imperial-ton, us-ton, st, oz");
    unit1 = input("Which unit would you like to convert from: ");
    unit2 = input("Which unit would you like to convert to: ");
    num1 = input("Enter your value: " );
    weightcalc(unit1, unit2, num1);

def weightcalc(unit1, unit2, num1):

#----------//Grammes\\----------#
    if unit1 == "g" and unit2 == "kg":
        ans = float(num1) / 1000;
    elif unit1 == "g" and unit2 == "ug":
        ans = float(num1) * 1000000;
    elif unit1 == "g" and unit2 == "lbs":
        ans = float(num1) / 453.592;
    elif unit1 == "g" and unit2 == "tn":
        ans = float(num1) / 1000000;
    elif unit1 == "g" and unit2 == "mg":
        ans = float(num1) * 1000;
    elif unit1 == "g" and unit2 == "imperial-ton":
        ans = float(num1) / 1016000000;
    elif unit1 == "g" and unit2 == "us-ton":
        ans = float(num1) / 907184.74;
    elif unit1 == "g" and unit2 == "st":
        ans = float(num1) / 6350.293;
    elif unit1 == "g" and unit2 == "oz":
        ans = float(num1) / 28.35;
        
#----------//Kilograumes\\-----------#
    elif unit1 == "kg" and unit2 == "g":
        ans = float(num1) / 1000;
    elif unit1 == "kg" and unit2 == "ug":
        ans = float(num1) * 1000000000;
    elif unit1 == "kg" and unit2 == "tn":
        ans = float(num1) / 1000;
    elif unit1 == "kg" and unit2 == "lbs":
        ans = float(num1) * 2.205;
    elif unit1 == "kg" and unit2 == "mg":
        ans = float(num1) * 1000000;
    elif unit1 == "kg" and unit2 == "imperial-ton":
        ans = float(num1) / 1016.047;
    elif unit1 == "kg" and unit2 == "us-ton":
        ans = float(num1) / 907.185;
    elif unit1 == "kg" and unit2 == "st":
        ans = float(num1) * 6.35;
    elif unit1 == "kg" and unit2 == "oz":
        ans = float(num1) * 35.274;
        
#----------//Tonnes\\----------#
    elif unit1 == "tn" and unit2 == "g":
        ans = float(num1) * 1000000;
    elif unit1 == "tn" and unit2 == "kg":
        ans = float(num1) * 1000;
    elif unit1 == "tn" and unit2 == "lbs":
        ans = float(num1) * 2204.623;
    elif unit1 == "tn" and unit2 == "ug":
        ans = float(num1) * 1000000000000;
    elif unit1 == "tn" and unit2 == "mg":
        ans = float(num1) * 1000000000;
    elif unit1 == "tn" and unit2 == "imperial-ton":
        ans = float(num1) / 1.016;
    elif unit1 == "tn" and unit2 == "us-ton":
        ans = float(num1) * 1.102;
    elif unit1 == "tn" and unit2 == "st":
        ans = float(num1) * 157.473;
    elif unit1 == "tn" and unit2 == "oz":
        ans = float(num1) * 35273.962;
        
#----------//Micrograumes\\----------#
    elif unit1 == "ug" and unit2 == "g":
        ans = float(num1) / 1000000;
    elif unit1 == "ug" and unit2 == "kg":
        ans = float(num1) / 1000000000;
    elif unit1 == "ug" and unit2 == "tn":
        ans = float(num1) / 1000000000000;
    elif unit1 == "ug" and unit2 == "lbs":
        ans = float(num1) / 453600000;
    elif unit1 == "ug" and unit2 == "mg":
        ans = float(num1) / 1000;
    elif unit1 == "ug" and unit2 == "imperial-ton":
        ans = float(num1) / 1016000000000;
    elif unit1 == "ug" and unit2 == "us-ton":
        ans = float(num1) / ((9.072*10)**11);
    elif unit1 == "ug" and unit2 == "st":
        ans = float(num1) / ((6.35*10)**9);
    elif unit1 == "ug" and unit2 == "oz":
        ans = float(num1) * ((2.835*10)**7);
        
#----------//Milligraumes\\----------#
    elif unit1 == "mg" and unit2 == "ug":
        ans = float(num1) * 1000;
    elif unit1 == "mg" and unit2 == "kg":
        ans = float(num1) / 1000000;
    elif unit1 == "mg" and unit2 == "tn":
        ans = float(num1) / 1000000000;
    elif unit1 == "mg" and unit2 == "lbs":
        ans = float(num1) / 453592.37;
    elif unit1 == "mg" and unit2 == "g":
        ans = float(num1) / 1000;
    elif unit1 == "mg" and unit2 == "imperial-ton":
        ans = float(num1) / 1016000000;
    elif unit1 == "mg" and unit2 == "us-ton":
        ans = float(num1) * ((9.072*10)**8);
    elif unit1 == "mg" and unit2 == "st":
        ans = float(num1) / ((6.35*10)**6);
    elif unit1 == "mg" and unit2 == "oz":
        ans = float(num1) / 28349.523;
        
#----------//Pounds\\----------#
    elif unit1 == "lbs" and unit2 == "tn":
        ans = float(num1) / 2204.623;
    elif unit1 == "lbs" and unit2 == "g":
        ans = float(num1) * 453.592;
    elif unit1 == "lbs" and unit2 == "kg":
        ans = float(num1) / 2.205;
    elif unit1 == "lbs" and unit2 == "ug":
        ans = float(num1) * 453600000;
    elif unit1 == "lbs" and unit2 == "mg":
        ans = float(num1) * 453592.37;
    elif unit1 == "lbs" and unit2 == "imperial-ton":
        ans = float(num1) / 2240;
    elif unit1 == "lbs" and unit2 == "us-ton":
        ans = float(num1) / 2000;
    elif unit1 == "lbs" and unit2 == "st":
        ans = float(num1) / 14;
    elif unit1 == "lbs" and unit2 == "oz":
        ans = float(num1) * 16;
        
#----------//Imperial Tonne\\----------#
    elif unit1 == "imperial-ton" and unit2 == "lbs":
        ans = float(num1) * 2240;
    elif unit1 == "imperial-ton" and unit2 == "tn":
        ans = float(num1) * 1.016;
    elif unit1 == "imperial-ton" and unit2 == "g":
        ans = float(num1) * 1016000000;
    elif unit1 == "imperial-ton" and unit2 == "kg":
        ans = float(num1) * 1016.047;
    elif unit1 == "imperial-ton" and unit2 == "ug":
        ans = float(num1) * 1016000000000000;
    elif unit1 == "imperial-ton" and unit2 == "mg":
        ans = float(num1) * 1016000000000;
    elif unit1 == "imperial-ton" and unit2 == "us-ton":
        ans = float(num1) * ((1.016*10)**12);
    elif unit1 == "imperial-ton" and unit2 == "st":
        ans = float(num1) * 160;
    elif unit1 == "imperial-ton" and unit2 == "oz":
        ans = float(num1) * 35840;
        
#----------//US-Ton\\----------#
    elif unit1 == "us-ton" and unit2 == "lbs":
        ans = float(num1) * 2000;
    elif unit1 == "us-ton" and unit2 == "tn":
        ans = float(num1) / 1.102;
    elif unit1 == "us-ton" and unit2 == "g":
        ans = float(num1) * 907184.74;
    elif unit1 == "us-ton" and unit2 == "kg":
        ans = float(num1) * 907.185;
    elif unit1 == "us-ton" and unit2 == "ug":
        ans = float(num1) * ((9.072*10)**11);
    elif unit1 == "us-ton" and unit2 == "mg":
        ans = float(num1) * ((9.072*10)**8);
    elif unit1 == "us-ton" and unit2 == "imperial-ton":
        ans = float(num1) / 1.12;
    elif unit1 == "us-ton" and unit2 == "st":
        ans = float(num1) * 142.857;
    elif unit1 == "us-ton" and unit2 == "oz":
        ans = float(num1) * 32000;
        
#----------//Stone\\----------#
    elif unit1 == "st" and unit2 == "lbs":
        ans = float(num1) * 14;
    elif unit1 == "st" and unit2 == "tn":
        ans = float(num1) / 157.473;
    elif unit1 == "st" and unit2 == "g":
        ans = float(num1) * 6350.293;
    elif unit1 == "st" and unit2 == "kg":
        ans = float(num1) * 6.35;
    elif unit1 == "st" and unit2 == "ug":
        ans = float(num1) * (6.35*10**9);
    elif unit1 == "st" and unit2 == "mg":
        ans = float(num1) * ((6.35*10)**6);
    elif unit1 == "st" and unit2 == "imperial-ton":
        ans = float(num1) / 160;
    elif unit1 == "st" and unit2 == "oz":
        ans = float(num1) * 224;
    elif unit1 == "st" and unit2 == "us-ton":
        ans = float(num1) / 142.857;

#----------//Ounces\\----------#
    elif unit1 == "oz" and unit2 == "lbs":
        ans = float(num1) / 16;
    elif unit1 == "oz" and unit2 == "tn":
        ans = float(num1) / 35273.962;
    elif unit1 == "oz" and unit2 == "g":
        ans = float(num1) * 28.35;
    elif unit1 == "oz" and unit2 == "kg":
        ans = float(num1) / 35.274;
    elif unit1 == "oz" and unit2 == "ug":
        ans = float(num1) * ((2.835*10)**7);
    elif unit1 == "oz" and unit2 == "mg":
        ans = float(num1) * 28349.523;
    elif unit1 == "oz" and unit2 == "imperial-ton":
        ans = float(num1) / 35840;
    elif unit1 == "oz" and unit2 == "us-ton":
        ans = float(num1) / 32000;
    elif unit1 == "oz" and unit2 == "st":
        ans = float(num1) / 224;
        
#----------//Input Validation\\----------#
    elif unit1 == unit2: 
        ans = num1;
        
#----------//Suffixes\\----------#
    if unit2 == "lbs":
      print(str(ans) + " Pounds\n");
    elif unit2 == "tn":
      print(str(ans) + " Tonnes\n");
    elif unit2 == "g":
      print(str(ans) + " Grammes\n");
    elif unit2 == "kg":
      print(str(ans) + " Kilogrammes\n");
    elif unit2 == "ug":
      print(str(ans) + " Microgrammes\n");
    elif unit2 == "mg":
      print(str(ans) + " Milligrammes\n");
    elif unit2 == "imperial-ton":
      print(str(ans) + " Imperial Tonnes\n");
    elif unit2 == "us-ton":
      print(str(ans) + " US Tonnes\n");
    elif unit2 == "st":
      print(str(ans) + " Stones\n");
    elif unit2 == "oz":
      print(str(ans) + " Ounces\n");
      
def radio_calculation_calculator(selector1, c):
    selector1 = float(input("Which category would you like to convert? we support any of these topics, just type the number shown\n\n(1)  dBm To Watt Calculator\n(2)  Frequency to Wavelength\n(3)  Noise Factor to Noise Figure Calculator\n(4)  Noise Figure to Noise Temperature Calculator\n(5)  Noise Temperature to Noise Figure Convertor\n(6)  PPM to Hz Calculator\n(7)  SINAD to ENOB Calculator\n(8)  Watt To dBm Calculator\n(9)  Wavelength to Frequency\n"));
    input1 = 0;
    ans = 0;
    
    if((selector1) == (1)):
        input1 = float(input("\nenter dBm value to convert it to Watts\n\n"));
        ans = ((10**(float(input1)/10))/ 1000);
        print("With a dBm value of", input1, "dBm, your expected wattage would be", round(ans, 4), "Watts \n");

    if(selector1 == 2):
        unit = float(input("What unit of frequency are you entering your input in?\n\n (1) Hz\n (2) kHz\n (3) MHz\n (4) GHz\n\n"));

        if(unit == 1):
            Hz(c, input1, unit1);
        if(unit == 2):
            kHz(c, input1, unit1);
        if(unit == 3):
            MHz(c, input1, unit1);
        if(unit == 4):
            GHz(c, input1, unit1);
            
    elif(selector1 == 3):
        value = float(input("Please enter your noise factor (0 to 1)\n\n"));

        if value == 0:
            print("Your Calculated Noise Figure Value is -∞dB");
        else:
            print("Your Calculated Noise Figure Value is", (10 * (math.log10(value))), "dB");

    elif(selector1 == 4):

        nfig = 0;
        tref = 0;

        tref = float(input("Please enter the reference temperature in Kelvin (Usually 290K)\n\n"));
        nfig = float(input("Please enter the Noise Figure\n\n"));

        ans = tref * (pow(10,nfig/10)-1);
        print(ans, "Kelvin");

    elif (selector1 == 5):
        ntemp = 0;
        tref = 0;

        tref = float(input("Please enter the reference temperature in Kelvin (Usually 290K)\n\n"));
        ntemp = float(input("Please enter the noise temperature\n\n"));

        print(str(10 * math.log(ntemp / tref + 1) / math.log(10)) + " dB");


    elif(selector1 == 6):

        unit = float(input("What unit of oscillation frequency are you entering your input in?\n\n (1) Hz\n (2) kHz\n (3) MHz\n (4) GHz\n\n"));

        if(unit == 1):
            PPMHz(c, input1, unit1);
        if(unit == 2):
            PPMkHz(c, input1, unit1);
        if(unit == 3):
            PPMMHz(c, input1, unit1);
        if(unit == 4):
            PPMGHz(c, input1, unit1);
                

    elif(selector1 == 7):

        sinad = float(input("Please enter the Value of SINAD in dB\n\n"))
        ans = (( (sinad) - (1.76)) / ( 6.02 ))
        print("With a SINAD Value of", sinad, "dB, Your calculated ENOB Value is", ans, "Bits")
    elif(selector1 == 8):

        Watts = float(input("\nPlease enter your wattage in Watts\n\n"))
        ans = ((10) * math.log10(Watts) + (30))
        print("With a wattage of", Watts, "Watt(s), your calculated dBm would be", ans ,"dBm")        

    elif(selector1 == 9):

        Lambda = float(input("Please enter your wavelength in Metres\n\n"));
        unit = float(input("What unit of frequency are you expecting your output in?\n\n (1) Hz\n (2) kHz\n (3) MHz\n (4) GHz\n\n"));

        if(unit == 1):
            WavHz(c, Lambda);
        if(unit == 2):
            WavkHz(c, Lambda);
        if(unit == 3):
            WavMHz(c, Lambda);
        if(unit == 4):
            WavGHz(c, Lambda);

def WavHz(c, Lambda):
            ans = ((c) / Lambda);
            print("With a Wavelength of", Lambda,"Metres, This wavelength's frequency in air is", ans, "Hz");

def WavkHz(c, Lambda):
            ans = ((c) / ((Lambda) * 1000));
            print("With a Wavelength of", Lambda,"Metres, This wavelength's frequency in air is", ((ans)/(1000)), "kHz");
  
def WavMHz(c, Lambda):
            ans = ((c) / Lambda);
            print("With a Wavelength of", Lambda,"Metres, This wavelength's frequency in air is", ((ans)/(1000000)), "MHz");
     
def WavGHz(c, Lambda):
            ans = ((c) / Lambda);
            print("With a Wavelength of", Lambda,"Metres, This wavelength's frequency in air is", ((ans)/(1000000000)), "GHz");


def Hz(c, input1, unit1):
            input1 = float(input("Please enter your frequency in Hertz\n\n"));
            ans = ((c) / input1);
            print("With a frequency of", input1,"Hz, This frequency's wavelength in air is", ans, "Metres");

def kHz(c, input1, unit1):
            input1 = float(input("Please enter your frequency in kHz\n\n"));
            ans = ((c) / (input1  * (10**3)));
            print("With a frequency of", input1,"kHz, This frequency's wavelength in air is", ans, "Metres");
            
def MHz(c, input1, unit1):
            input1 = float(input("Please enter your frequency in MHz\n\n"));
            ans = ((c) / (input1  * (10**6)));
            print("With a frequency of", input1, "MHz, This frequency's wavelength in air is", ans, "Metres");
            
def GHz(c, input1, unit1):
            input1 = float(input("Please enter your frequency in GHz\n\n"));
            ans = ((c) / (input1  * (10**9)));
            print("With a frequency of", input1, "GHz, This frequency's wavelength in air is", ans, "Metres");



def PPMHz(c, input1, unit1):
            input1 = float(input("Please enter your oscillation frequency in Hertz\n\n"));
            PPM = float(input("Please enter Frequency Stability in PPM (Parts Per Million)\n\n"))
            ans = ((input1 * PPM) / (10**6))
            print("With an Oscillation frequency of",input1,"Hz, and a PPM of", PPM, "PPM, Your outputted Hz Value is", ans, "Hz");

def PPMkHz(c, input1, unit1):
            input1 = float(input("Please enter your oscillation frequency in Kilohertz\n\n"));
            PPM = float(input("Please enter Frequency Stability in PPM (Parts Per Million)\n\n"))
            ans = ((((input1) * (1000)) * (PPM)) / (10**6));
            print("With an Oscillation frequency of",input1,"KHz, and a PPM of", PPM, "PPM, Your outputted Hz Value is", ans, "Hz");
            
def PPMMHz(c, input1, unit1):
            input1 = float(input("Please enter your oscillation frequency in Megahertz\n\n"));
            PPM = float(input("Please enter Frequency Stability in PPM (Parts Per Million)\n\n"))
            ans = ((((input1) * (10000)) * (PPM)) / (10**6));
            print("With an Oscillation frequency of",input1,"MHz, and a PPM of", PPM, "PPM, Your outputted Hz Value is", ans, "Hz");
           
def PPMGHz(c, input1, unit1):
            input1 = float(input("Please enter your oscillation frequency in Gigahertz\n\n"));
            PPM = float(input("Please enter Frequency Stability in PPM (Parts Per Million)\n\n"))
            ans = ((((input1) * (10000)) * (PPM)) / (10**6));
            print("With an Oscillation frequency of",input1,"GHz, and a PPM of", PPM, "PPM, Your outputted Hz Value is", ans, "Hz");
   

def radio_calculation_calculatorcalc(selector1, c):

    if(selector1 == 2):
        unit = input("What unit of frequency are you entering your input in?\n\n (1) Hz\n (2) kHz\n (3) MHz\n (4) GHz");
        if unit == 1:
            unit1 == "Hz";
            input1 = input("Please enter your frequency in", unit1);
            ans = ((c) / input1);
            print("With a frequency of", input1, unit1, "This frequency's wavelength in air is", ans, "Metres");
        elif unit == 2:
            unit1 == "kHz";
            input1 = input("Please enter your frequency in", unit1);
            ans = ((c) / (input1  * (10**3)));
            print("With a frequency of", input1, unit1, "This frequency's wavelength in air is", ans, "Metres");
        elif unit == 3:
            unit1 == "MHz";
            input1 = input("Please enter your frequency in", unit1);
            ans = ((c) / (input1  * (10**6)));
            print("With a frequency of", input1, unit1, "This frequency's wavelength in air is", ans, "Metres");
        elif unit == 4:
            unit1 == "GHz";
            input1 = input("Please enter your frequency in", unit1);
            ans = ((c) / (input1  * (10**9)));
            print("With a frequency of", input1, unit1, "This frequency's wavelength in air is", ans, "Metres");
            ans = ((c) / input1);
        print("With a frequency of", input1, unit1, "This frequency's wavelength in air is", ans, "Metres");

def antenna_calculator():

    selector1 = float(input("\nWhich category would you like to convert? we support any of these topics, just type the number shown\n\n(1) Antenna Downtilt Angle\n\n"));

    if ((selector1) == (1)):

        selector = float(input("\nPlease enter the unit of height you are entering your input in\n\n(1) Feet\n(2) Metres\n\n"));

        if selector == 1:
            unit = "Feet";
            Hb = float(input("\nPlease enter the height of the Base Antenna in Feet\n"));
            Hr = float(input("Please enter the height of the Remote Antenna in Feet\n"));
            DistUnit = float(input("Please enter the unit of distance you are entering your input in\n\n(1) Kilometres\n(2) Miles"));
            
            if DistUnit == 1:
                Dist = float(input("Please enter the distance between the base and remote station in Kilometres"));

            if DistUnit == 2:
                Dist = float(input("Please enter the distance between the base and remote station in Miles"));
            
        elif selector == 2:
            unit = "Metres";    
            Hb = float(input("\nPlease enter the height of the Base Antenna in Metres\n"));
            Hr = float(input("Please enter the height of the Remote Antenna in Metres\n"));
            Dist = float(input("Please enter the unit of distance you are entering your input in\n\n"));
            
            if DistUnit == 1:
                Dist = float(input("Please enter the distance between the base and remote station in Kilometres"));

            if DistUnit == 2:
                Dist = float(input("Please enter the distance between the base and remote station in Miles"));
                
# def attenuator_calculator():
# def microstrip_calculator():
# def radar_calculator():
# def rf_calculator():
def waveguide_calculator():
    selector1 = float(input("Which category would you like to convert? we support any of these topics, just type the number shown\n\n(1) Cavity Resonance Frequency\n(2) Circular Waveguide Calculator\n(3) Rectangular Waveguide Cut-off Frequency\n"));

    if ((selector1) == (1)):
        width = float(input("Please enter the cavity width\n"));
        length = float(input("Please enter the cavity length\n"));
        height = float(input("Please enter the cavity height\n"));
        m = float(input("Please enter the M(Mode number) \n"));             
        n = float(input("Please enter the N(Mode number) \n"));
        p = float(input("Please enter the P(Mode number) \n"));
        diconst = float(input("Please enter the Dialectric Constant of the material\n"));
        magperm = float(input("Please enter the Magnetic Permeability of the material\n"));
        print("These are test values, cavity resonance is not easy to calculate the math for correctly -", width, length, height, m, n, p, diconst, magperm);
        print("This will be worked on last");
#----------//Main\\----------#
print("Welcome to my convertor, please follow me on GitHub if it's useful! :)\n");

selector = input("Which category would you like to convert? we support any of these topics, just type the number shown to see all subjects within it > \n\n(1)  Length\n(2)  Weight\n(3)  Radio conversion calculators\n(4)  Antenna Calculators// Not Working\n(5)  Attenuator Calculators// Not Working\n(6)  Microstrip Calculators// Not Working\n(7)  Radar Calculators// Not Working\n(8)  RF Calculators// Not Working\n(9)  Waveguide Calculators// Not Working\n(10) My Github\n(11) Exit Programme\n\n");

if ((float(selector)) == (1)):
    length();
elif ((float(selector)) == (2)):
    weight();
elif ((float(selector)) == (3)):
    radio_calculation_calculator(selector1, c);
elif ((float(selector)) == (4)):
    antenna_calculator();
elif ((float(selector)) == (5)):
    attenuator_calculator();
elif ((float(selector)) == (6)):
    microstrip_calculator();
elif ((float(selector)) == (7)):
    radar_calculator();
elif ((float(selector)) == (8)):
    rf_calculator();
elif ((float(selector)) == (9)):
    waveguide_calculator();
elif ((float(selector)) == (10)):
    webbrowser.open("https://github.com/AxiomYT/");
elif ((float(selector)) == (11)):
    raise SystemExit;

#----------//\\----------#
