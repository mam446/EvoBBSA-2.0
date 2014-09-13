



{
    'hyperSettings':
    {
        'runName':"testRun",
        'runNumber':0,
        'mu':100,
        'lambda':40,
        'type':'nsga',#this can be SGA or nsga
        'mpi':True,
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
        'maxStartNodes':30,
        'maxEvals':100000,
        'maxOps':5000000,
        'maxIterations':10000,
        'maxDepth':7,
        'mutateMax':7,
        'runs':5,
        'converge':25,
        'initPopMax':100,
        'representation':'bitString',
        'problem':'dTrap',
        'penalty':.001,
        'time':20
    },
    
    
        'problems':
    [
        {
            'weight':1,
            'repr':'bitString',
            'prob':'lSat',
            'settings':
            {
                'name':'test4.cnf',
                'length':216,
            }
        },
        {
            'weight':1,
            'repr':'bitString',
            'prob':'lSat',
            'settings':
            {
                'name':'test5.cnf',
                'length':343,
            }
        },



    ],
    
    'nodeSettings':
    {
        'randInd':
        {
            'count':
            {
                'value':1,
                'range':(1,25),
                'type':'int',
            },
            'weight':2,
        },
        'ifConverge':
        {
            'conv':
            {
                'value':5,
                'range':(5,25),
                'type':'int'
            },
            'reset':
            {
                'value':False,
                'range':[True,False],
                'type':'bool',
            },
            'weight':2
        },
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







