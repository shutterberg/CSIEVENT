from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, SubmitField
from wtforms.validators import DataRequired

class KeyForm(FlaskForm):
  teamnum = IntegerField('Team Number',validators=[DataRequired()])  
  key = StringField('Key',validators=[DataRequired()])
  submit = SubmitField('Submit') 

app=Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

dict={}
rnd={2.0:2.1,2.1:2.2,2.2:2.3,2.3:2.4}



@app.route('/')
def index():
    return render_template('base.html',round_num=2.1)

@app.route('/home')
def home():
    return render_template('base.html')  

@app.route('/level',methods=['GET','POST'])
def level():
  
  form = KeyForm(csrf_enabled=False)
  if form.validate_on_submit():
    if form.key.data=='rnd1':
        round_num=2.1
        dict[form.teamnum.data]=2.1
        print(dict)
        return render_template('display.html',form=form,round_num=2.2)
    elif form.key.data=='rnd2':
        round_num=2.2
        dict[form.teamnum.data]=2.2
        print(dict)
        return render_template('display.html',form=form,round_num=2.3)    
    elif form.key.data=='rnd3':
        round_num=2.3
        dict[form.teamnum.data]=2.3
        print(dict)
        return render_template('display.html',form=form,round_num=2.4)
    elif form.key.data=='rnd4':
        round_num=2.4
        dict[form.teamnum.data]=2.4
        print(dict)
        tnm='LWZ'+str((form.teamnum.data*10))+str(3216952*form.teamnum.data)
        return render_template('congrats.html',teamnum=tnm)        
    else:
        flash('Invalid Key','error')
        if dict.get(form.teamnum.data,2.0)==2.0:
            return render_template('level.html',form=form,round_num=2.1)
        else:     
            return render_template('display.html',form=form,round_num=(rnd[dict.get(form.teamnum.data,2.0)]))   
  return render_template('level.html',form=form,round_num=2.1) 
