
function model = histones_preequ_Zheng_syms()

syms t
model.param = 'log10';



syms K27me0K36me0 K27me0K36me1 K27me1K36me0 K27me0K36me2 K27me1K36me1 K27me2K36me0 K27me0K36me3 K27me1K36me2 K27me2K36me1 K27me3K36me0 K27me1K36me3 K27me2K36me2 K27me3K36me1 K27me2K36me3 K27me3K36me2
syms inflow k00_01 k00_10 k01_00 k01_02 k01_11 k02_01 k02_03 k02_12 k03_02 k03_13 k10_00 k10_11 k10_20 k11_01 k11_10 k11_12 k11_21 k12_02 k12_11 k12_13 k12_22 k13_03 k13_12 k13_23 k20_10 k20_21 k20_30 k21_11 k21_20 k21_22 k21_31 k22_12 k22_21 k22_23 k22_32 k23_13 k23_22 k30_20 k30_31 k31_21 k31_30 k31_32 k32_22 k32_31 sigmaY

model.sym.x = [K27me0K36me0, K27me0K36me1, K27me1K36me0, K27me0K36me2, K27me1K36me1, K27me2K36me0, K27me0K36me3, K27me1K36me2, K27me2K36me1, K27me3K36me0, K27me1K36me3, K27me2K36me2, K27me3K36me1, K27me2K36me3, K27me3K36me2];


model.sym.p = [inflow k00_01, k00_10, k01_00, k01_02, k01_11, k02_01, k02_03, k02_12, k03_02, k03_13, k10_00, k10_11, k10_20, k11_01, k11_10, k11_12, k11_21, k12_02, k12_11, k12_13, k12_22, k13_03, k13_12, k13_23, k20_10, k20_21, k20_30, k21_11, k21_20, k21_22, k21_31, k22_12, k22_21, k22_23, k22_32, k23_13, k23_22, k30_20, k30_31, k31_21, k31_30, k31_32, k32_22, k32_31, sigmaY];

model.sym.xdot = [inflow - K27me0K36me0*inflow - K27me0K36me0*k00_01 - K27me0K36me0*k00_10 + K27me0K36me1*k01_00 + K27me1K36me0*k10_00,...
    K27me0K36me0*k00_01 - K27me0K36me1*inflow - K27me0K36me1*k01_00 - K27me0K36me1*k01_02 - K27me0K36me1*k01_11 + K27me0K36me2*k02_01 + K27me1K36me1*k11_01,...
    K27me0K36me0*k00_10 - K27me1K36me0*inflow - K27me1K36me0*k10_00 - K27me1K36me0*k10_11 - K27me1K36me0*k10_20 + K27me1K36me1*k11_10 + K27me2K36me0*k20_10,...
    K27me0K36me1*k01_02 - K27me0K36me2*inflow - K27me0K36me2*k02_01 - K27me0K36me2*k02_03 - K27me0K36me2*k02_12 + K27me0K36me3*k03_02 + K27me1K36me2*k12_02,...
    K27me0K36me1*k01_11 - K27me1K36me1*inflow + K27me1K36me0*k10_11 - K27me1K36me1*k11_01 - K27me1K36me1*k11_10 - K27me1K36me1*k11_12 - K27me1K36me1*k11_21 + K27me1K36me2*k12_11 + K27me2K36me1*k21_11,...
    K27me1K36me0*k10_20 - K27me2K36me0*inflow - K27me2K36me0*k20_10 - K27me2K36me0*k20_21 - K27me2K36me0*k20_30 + K27me2K36me1*k21_20 + K27me3K36me0*k30_20,...
    K27me0K36me2*k02_03 - K27me0K36me3*inflow - K27me0K36me3*k03_02 - K27me0K36me3*k03_13 + K27me1K36me3*k13_03,...
    K27me0K36me2*k02_12 - K27me1K36me2*inflow + K27me1K36me1*k11_12 - K27me1K36me2*k12_02 - K27me1K36me2*k12_11 - K27me1K36me2*k12_13 - K27me1K36me2*k12_22 + K27me1K36me3*k13_12 + K27me2K36me2*k22_12,...
    K27me1K36me1*k11_21 - K27me2K36me1*inflow + K27me2K36me0*k20_21 - K27me2K36me1*k21_11 - K27me2K36me1*k21_20 - K27me2K36me1*k21_22 - K27me2K36me1*k21_31 + K27me2K36me2*k22_21 + K27me3K36me1*k31_21,...
    K27me2K36me0*k20_30 - K27me3K36me0*inflow - K27me3K36me0*k30_20 - K27me3K36me0*k30_31 + K27me3K36me1*k31_30,...
    K27me0K36me3*k03_13 - K27me1K36me3*inflow + K27me1K36me2*k12_13 - K27me1K36me3*k13_03 - K27me1K36me3*k13_12 - K27me1K36me3*k13_23 + K27me2K36me3*k23_13,...
    K27me1K36me2*k12_22 - K27me2K36me2*inflow + K27me2K36me1*k21_22 - K27me2K36me2*k22_12 - K27me2K36me2*k22_21 - K27me2K36me2*k22_23 - K27me2K36me2*k22_32 + K27me2K36me3*k23_22 + K27me3K36me2*k32_22,...
    K27me2K36me1*k21_31 - K27me3K36me1*inflow + K27me3K36me0*k30_31 - K27me3K36me1*k31_21 - K27me3K36me1*k31_30 - K27me3K36me1*k31_32 + K27me3K36me2*k32_31,...
    K27me1K36me3*k13_23 - K27me2K36me3*inflow + K27me2K36me2*k22_23 - K27me2K36me3*k23_13 - K27me2K36me3*k23_22,...
    K27me2K36me2*k22_32 - K27me3K36me2*inflow + K27me3K36me1*k31_32 - K27me3K36me2*k32_22 - K27me3K36me2*k32_31];

model.sym.k = [];

model.sym.x0 = sym(zeros(15,1));

model.sym.y = model.sym.x;
model.sym.sigma_y = sym(ones(15,1) .* sigmaY);

