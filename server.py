from flask import Flask, render_template, request

app = Flask(__name__)

LENGTH = ["km","m","cm","mm","in","ft","yd","mi"]
WEIGHT = ["t","kg","g","mg"]
TEMPERATURE = ["C","F","K"]


@app.route("/",methods=["GET","POST"])
def index():
    Uvalue = None
    unit = None
    final_value = None
    tunit = None
    error = None

    if request.method == "POST":
        length = request.form.get("length")
        if length and length.strip():
            unit = request.form.get("unit")
            tunit = request.form.get("tunit")

            def convert_length(value,from_unit,to_unit):
                units = {'km': 1000, 'm': 1, 'cm': 0.01, 'mm': 0.001,'in':0.0254,
                        'ft':0.3048,'yd':0.9144,'mi':1609.344}
                return float(value) * units[from_unit] / units[to_unit]
            
            c_unit = convert_length(length,unit,tunit) 

            final_value = round(c_unit,6) 
            Uvalue = length
        else:
            error = "enter valid units"

    return render_template("index.html",length_units = LENGTH,orignal_value=Uvalue,
                           unit=unit,
                           cunit=final_value,tunit=tunit,error=error)

@app.route("/weight",methods=["GET","POST"])
def weight():
    Uvalue = None
    unit = None
    final_value = None
    tunit = None
    error = None

    if request.method == "POST":
        weight = request.form.get("weight")
        if  weight and weight.strip():
            unit = request.form.get("unit")
            tunit = request.form.get("tunit")

            def convert_weight(value,from_unit,to_unit):
                units = { 't':1000000,'kg':1000,'g':1,'mg':0.001,'oz':28.3495,'lb':453.592}
                return float(value) * units[from_unit] / units[to_unit]
            
            w_unit = convert_weight(weight,unit,tunit)

            final_value = round(w_unit,6)
            Uvalue = weight
        else:
            error = "enter valid units"
    return render_template('weight.html',weight_units = WEIGHT,
                           orignal_value=Uvalue,unit=unit,
                           cunit=final_value,tunit=tunit,error=error)


@app.route('/temperature',methods=["GET","POST"])
def temperature():
    Uvalue = None
    unit = None
    final_value = None
    tunit = None
    error = None

    if request.method == "POST":
        temperature = request.form.get("temperature")
        if temperature and temperature.strip:
            unit = request.form.get("unit")
            tunit = request.form.get("tunit")

            def convert_temperature(value, from_unit, to_unit):

                from_unit = from_unit.lower()
                to_unit = to_unit.lower()
                
                # First convert to Celsius
                if from_unit == 'c':
                    c = value
                elif from_unit == 'f':
                    c = (value - 32) * 5/9
                elif from_unit == 'k':
                    c = value - 273.15
                else:
                    error = "Please enter a valid units!"
                
                # Then convert from Celsius to target
                if to_unit == 'c':
                    return c
                elif to_unit == 'f':
                    return c * 9/5 + 32
                elif to_unit == 'k':
                    return c + 273.15
                else:
                    error = "Please enter a valid units!"
        
            final_value = convert_temperature(float(temperature),unit,tunit)
            Uvalue = temperature
        
    return render_template('temperature.html',
                           temperature_units = TEMPERATURE,
                           orignal_value=Uvalue,
                           unit=unit,cunit=final_value,
                           tunit=tunit,error= error)



    

