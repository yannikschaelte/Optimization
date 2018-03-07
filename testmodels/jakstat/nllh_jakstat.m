function [ varargout ] = nllh_jakstat(theta, D)

amiOptions.rtol = 1e-12;
amiOptions.atol = 1e-14;
amiOptions.sensi_meth = 'adjoint';

% for every experiment and replicate, do the optimization
n_e = size(D,2);

% disp(num2str(nargout));

% prepare output and sensi
switch nargout
    case 1
        varargout{1} = 0;
        amiOptions.sensi = 0;
    case 2
        varargout{1} = 0;
        varargout{2} = 0;
        amiOptions.sensi = 1;
    case 3
        varargout{1} = 0;
        varargout{2} = 0;
        varargout{3} = 0;
        amiOptions.sensi = 2;
    otherwise
        error('Only supports up to 3 outputs.');
end

for ie = 1:n_e
    n_r = size(D(ie).Y,3);
    for ir = 1:n_r
        
        % set data for simulation
        clear amiData;
        amiData.t = D(ie).t;
        amiData.Y = D(ie).Y(:,:,ir);
        amiData.Sigma_Y = nan(size(amiData.Y));
        amiData.condition = D(ie).k(:);
        amiData = amidata(amiData);
        
        sol = simulate_jakstat([], theta, [], amiData, amiOptions);
        
        switch amiOptions.sensi
            case 0
                varargout{1} = varargout{1} - sol.llh;
            case 1
                varargout{1} = varargout{1} - sol.llh;
                varargout{2} = varargout{2} - sol.sllh;
            case 2
                varargout{1} = varargout{1} - sol.llh;
                varargout{2} = varargout{2} - sol.sllh;
                varargout{3} = varargout{3} - sol.s2llh;
        end
       
    end
end

end
