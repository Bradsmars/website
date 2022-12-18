import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Bradley Marimbire.
##### *Resume* 
''')

image = Image.open('dp.png')
st.image(image, width=200)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
Data Science is the future and is the one cutting-edge technology that has and will continue to revolutionise
professional service firms. Having spent three years doing a data science undergraduate course, from my
experience, I developed an interest in pursuing a career as a data scientist due to part-taking in various
end-to-end projects. My undergraduate education prepared me with analytical, creative, and problem-solving
skills to work on diverse projects in different domains. By being exposed to core areas within data science, I
developed proficiency to an intermediate level in programming languages, including but not limited to R,
Python, NoSQL, and SQL. Furthermore, during my studies, I developed my analytical skills from a basic
understanding of data science to the advanced stage. The exposure provided me with in-depth knowledge of
various data science skills, tools, and methods for data analysis.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://github.com/Bradsmars" target="_blank">Bradley Marimbire</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#publications">Publications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**BTEC NATIONAL DIPLOMA** (Applied Medical Science), *Saint Francis Xavier Sixth Form College*, United Kingdom',
'2016-2018')
st.markdown('''
- Grade: `D*D*D*`
- Math modules: Applied mathematical tools In Science, Mathematical Calculations For Science, Using Statistics In Science, Medical Physics Techniques.
''')

txt('**Bachelors of Science** (Data Science), *Liverpool John Moores University*, United Kingdom',
'2019-2022')
st.markdown('''
- Grade: `2:1`
- Graduated with Upper 2:1 honours.
''')

#####################
st.markdown('''
## Publications
''')

txt('**Predicting the Effectiveness of ‘Stop and Search’ Police Interventions using advanced Analytics (Awaiting publication)**, Faculty of Computer Science & mathematics, Liverpool John Moores University, United Kingdom',
'2022')
st.markdown('''
My dissertation project is the first of its kind and achieved an accuracy of 93 percent. The proposed work presented
a crime prediction model using a stop search dataset and demographic of those charged with possessing a weapon.
The study used multiple publicly available datasets to predict the effectiveness of ‘stop and search’ interventions
conducted by the police in London.

''')

txt('**Jack Petchey Award**, Faculty of Medical Technology, aint Francis Xavier Sixth Form College, United kingdom',
'2016-2018')
st.markdown('''
I was awarded a certificate and grant price from the Jack Petchey foundation for my outstanding grades and
commitment to education. I donated the price money to help improve my college’s IT infrastructure.


''')


#####################
st.markdown('''
## Projects
''')
txt4('ABCpred', 'A web server for the discovery of acetyl- and butyryl-cholinesterase inhibitors', 'http://codes.bio/abcpred/')
txt4('AutoWeka', 'An automated data mining software based on Weka', 'http://www.mt.mahidol.ac.th/autoweka/')
txt4('ACPred', 'A computational tool for the prediction and analysis of anticancer peptides','http://codes.bio/acpred/')
txt4('BioCurator', 'A web server for curating ChEMBL bioactivity data', 'http://codes.bio/biocurator/')
txt4('CryoProtect', 'A web server for classifying antifreeze proteins from non-antifreeze proteins','http://codes.bio/cryoprotect/')
txt4('ERpred', 'A web server for the prediction of subtype-specific estrogen receptor antagonists', 'http://codes.bio/erpred')
txt4('HCVpred', 'A web server for predicting the bioactivity of Hepatitis C virus NS5B inhibitors', 'http://codes.bio/hemopred/')
txt4('HemoPred', 'A web server for predicting the hemolytic activity of peptides', 'http://codes.bio/hemopred/')
txt4('iQSP', 'A sequence-based tool for the prediction and analysis of quorum sensing peptides', 'http://codes.bio/iqsp/')
txt4('Meta-iAVP', 'A sequence-based meta-predictor for improving the prediction of antiviral peptides', 'http://codes.bio/meta-iavp/')
txt4('osFP', 'A web server for predicting the oligomeric state of fluorescent proteins', 'http://codes.bio/osfp/')
txt4('PAAP', 'A web server for predicting antihypertensive activity of peptides', 'http://codes.bio/paap/')
txt4('PepBio', 'A web server for predicting the bioactivity of host defense peptide', 'http://codes.bio/pepbio')
txt4('PyBact', 'Open source software written in Python for bacterial identification', 'https://sourceforge.net/projects/pybact/')
txt4('TargetAntiAngio', 'A sequence-based tool for the prediction and analysis of anti-angiogenic peptides','http://codes.bio/targetantiangio/')
txt4('ThalPred', 'Development of decision model for discriminating Thalassemia trait and Iron deficiency anemia','http://codes.bio/thalpred/')
txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`, `NoSQL`, `Tidyverse`, `Magrittr`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`, `Caret`, `Tidymodels`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/bradley-marimbire-analyst/')
txt2('GitHub', 'https://github.com/Bradsmars')
