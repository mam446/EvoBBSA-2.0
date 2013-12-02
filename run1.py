



{



    'bbsaSettings':
    {
        'maxStartNodes':15,
        'maxEvals':100000,
        'maxOps':5000000,
        'maxIterations':10000,
        'maxDepth':5,
        'mutateMax':5,
        'runs':5,
        'converge':25,
        'initPopMax':50,
        'probType':'bitString'
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


    ]

}







