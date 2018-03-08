classdef NoodleOptions < handle
    
    properties
        % optimizer options
        subproblem = SubproblemTR();
        
        % optimization options
        tol_step = 1e-10;
        tol_grad = 1e-5;
        iter_max = Inf;
        funeval_max = Inf;
        hessian_fcn = 'objective';
        verbosity   = 1;
        
        
    end
    
    methods
        
        function options = NoodleOptions(options_in)
            if isa(options_in,'NoodleOptions')
                options = options_in;
            elseif isa(options_in,'struct')
                fields_in = fields(options_in);
                for jf = 1:length(fields_in)
                    if ~isprop(options, fields_in{jf})
                        error(['Cannot assign options property ' fields_in{jf} ' to NoodleOptions.']);
                    end
                    options.(fields_in{jf}) = options_in.(fields_in{jf});            
                end
            else
                error('Invalid input for NoodleOptions');
            end
        end
        
    end
end
