ERROR_MAPPINGS={
    'apicast-staging':[
        {
            'error_trigger':"failed to get OIDC Provider",
            'message':{
                'pattern': "    [error] Invalid provider issuer: [{issuer}] check connectivity between APIcast and \"{host}\"",
                'params':{
                    'issuer':"Provider\sfrom\s(.+?)\s",
                    'host':"Provider\sfrom\s(http[s]:\/\/*.*?)[\/]"
                }
            }
        }
        ,
        {
            'error_trigger':"failed to connect to",
            'message':{
                'pattern': "    [error] Failed to connect to target: {target} \n            Check the target's logs and connectivity between APIcast and that URL.",
                'params':{
                    'target':"connect\sto\s(.*)"
                }
            }
        }
    ]
    ,
    'apicast-production':[
        {
            'error_trigger':"failed to get OIDC Provider",
            'message':{
                'pattern': "    [error] Invalid provider issuer: [{issuer}] check connectivity between APIcast and this host",
                'params':{
                    'issuer':"Provider\sfrom\s(.+?)\s"
                }
            }
        }
        ,
        {
            'error_trigger':"failed to connect to",
            'message':{
                'pattern': "    [error] Failed to connect to target: {target} \n            Check the target's logs and connectivity between APIcast and that URL.",
                'params':{
                    'target':"connect\sto\s(.*)"
                }
            }
        }
    ]
    ,
    'system-redis':[
        {
            'error_trigger':"Background AOF rewrite terminated",
            'message':{
                'pattern': "    [error] Failed AOF REWRITE: [{error_code}] check your storage for any errors.",
                'params':{
                    'error_code':"terminated\sby\s(.*)"
                }
            }
        }
    ]
}

