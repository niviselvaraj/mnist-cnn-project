echo"A script to create,activate and install requirements"
echo"............." 

virtualenv venv

echo"creation of virtualenve done"
echo"activation my env"
source venv/bin/activate

echo"............."
echo"install requirements.txt"
pip install -r requirements.txt

sleep(2)
echo"install done"
echo"Creation activation and installation of libraries"