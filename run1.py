



{



    'bbsaSettings':
    {
        'maxEvals':50000,
        'maxOps':5000000,
        'maxIterations':10000,
        'maxDepth':5,
        'mutateMax':5,
        'runs':5,
        'converge':25,
        'initPopMax':50
    },
    
    
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
     
    'problems':
    [
        {
            'weight':1,
            'repr':'bitstring',
            'prob':'dTrap',
            'settings':
            {
                'length':100,
                'k':5
            }
        },

        {
            'weight':1,
            'repr':'bitstring',
            'prob':'allOnes',
            'settings':
            {
                'length':210
            }
        },

        {
            'weight':1,
            'repr':'bitstring',
            'prob':'allOnes',
            'settings':
            {
                'length':100,
                'dimensions':30,
                'k':5,
                'problemSeed':0,
                'maximumFitness':1.0,
                'nkProblemFolder':'',
                'run':0
            }
        }

    ]

}







