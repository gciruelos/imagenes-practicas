import subprocess

EJ = 'ej2'
PARAM = 'c'
for image_name in ['lena', 'test']:
    for case in ['original', 'gauss10', 'gauss50', 'rayleigh15', 'saltpepper10']:
        in_img = 'practica6/ej1-imgs/'+image_name+'-'+case+'.png'
        out_img = 'practica6/informe-imgs/'+EJ+"-"+PARAM+"-"+image_name+'-'+case+'.pdf'
        bash_command = 'python3 practica6/'+EJ+'.py '+in_img+' '+PARAM+' '+out_img
        print(bash_command)
        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()


