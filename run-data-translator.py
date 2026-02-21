import numpy as np

path = '/mnt/storage/shared/jobs/01-sweep/output/TXCo11/simulation_data.npz'

dt = np.load(path)

# targets for both ffi and ffd
targets = dt['targets']
ffi = targets.reshape((260, 16000))
ffd = targets.reshape((520000, 8))

print('ffi', ffi.shape)
print('ffd', ffd.shape)

# ffi features
ffi_ft = dt['features'][:, :3]
print(ffi_ft)
print(ffi_ft.shape)

# ffd features
ffd_ft = ffi_ft.copy()

print(dt.keys)
print('features:        ', dt['features'].shape)
print('frequency points:', dt['frequency_points'].shape)
