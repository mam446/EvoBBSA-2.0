



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
        'maxEvals':50000,
        'maxOps':5000000,
        'maxIterations':10000,
        'maxDepth':5,
        'mutateMax':5,
        'runs':5,
        'converge':25,
        'initPopMax':50,
        'representation':'bitString',
        'problem':'nk',
        'time':20
    },
    'problems':
    [
        {
            'weight':1,
            'repr':'bitString',
            'prob':'nk',
            'settings':
            {
                'length':100,
                'k':5,
                'dimensions':30,
                'problemSeed':0,
                'nkProblemFolder':'./',
                'run':0
            }
        },

        {
            'weight':1,
            'repr':'bitString',
            'prob':'nk',
            'settings':
            {
                'length':100,
                'k':7,
                'dimensions':30,
                'problemSeed':1,
                'nkProblemFolder':'./',
                'run':1
            }
        },
        {
            'weight':1,
            'repr':'bitString',
            'prob':'nk',
            'settings':
            {
                'length':100,
                'k':5,
                'dimensions':30,
                'problemSeed':1,
                'nkProblemFolder':'./',
                'run':1
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







