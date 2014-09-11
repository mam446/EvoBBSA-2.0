



{
    'hyperSettings':
    {
        'runName':"testRun",
        'runNumber':0,
        'mu':100,
        'lambda':40,
        'type':'SGA',#this can be SGA or nsga
        'mpi':False,
        'procs':5,
        'mateRate':.3,
        'mutateRate':.3,
        'evaluations':5000,
        'objectives':['evals','fitness','time'],
        'childK':8,
        'seed':None,
        'hosts':[]
    },



    'bbsaSettings':
    {
        'maxStartNodes':15,
        'maxEvals':100000,
        'maxOps':5000000,
        'maxIterations':10000,
        'maxDepth':5,
        'mutateMax':5,
        'runs':5,
        'converge':30,
        'initPopMax':50,        
        'time':20,
        'penalty':.001,
        'representation':'bitString',
        'problem':'dTrap',

    },
    'problems':
    [
        {
            'weight':1,
            'repr':'bitString',
            'prob':'dTrap',
            'settings':
            {
                'length':100,
                'k':5
            }
        },

        {
            'weight':1,
            'repr':'bitString',
            'prob':'dTrap',
            'settings':
            {
                'length':210,
                'k':7
            }
        },


    ],
    
    'nodeSettings':
    {
        'mutate':
        {
            'rate':
            {
                'value':0.0,
                'range':(0.0,1.0),
                'type':'float'
            },
            'weight':2
        },
        'gaussian':
        {
            'rate':
            {
                'value':0.0,
                'range':(0.0,100.0),
                'type':'float'
            },
            'variance':
            {
                'value':0.0,
                'range':(0.0,1.0),
                'type':'float'
            },
            'weight':2
        },
        'uniRecomb':
        {
            'num':
            {
                'value':1,
                'range':(1,25),
                'type':'int'
            },
            'weight':2
        },
        'diagonal':
        {
            'n':
            {
                'value':1,
                'range':(1,25),
                'type':'int'
            },
            'weight':2
        },
        'onePoint':
        {
            'weight':2
        },
        'kTourn':
        {
            'k':
            {
                'value':1,
                'range':(1,25),
                'type':'int'
            },
            'count':
            {
                'value':1,
                'range':(1,25),
                'type':'int'
            },
            'weight':2
        },
        'trunc':
        {
            'count':
            {
                'value':1,
                'range':(1,25),
                'type':'int'
            },
            'weight':2
        },
        'randSubset':
        {
            'count':
            {
                'value':1,
                'range':(1,25),
                'type':'int'
            },
            'weight':2
        },
        'forLoop':
        {
            'count':
            {
                'value':1,
                'range':(1,25),
                'type':'int'
            },
            'weight':2
        },
        'makeSet':
        {
            'name':
            {
                'value':"",
                'type':'str'
            },
            'weight':2
        }

    },
     
    

}







