function get_sha256sum(record) {
    data = record[1] FS record[2] FS record[3]

    # always some discrepancies in calc-ing SHA256
    # echo plainly not working correctly
    #cmd = "echo -n \"" data "\" | sha256sum | awk '{print $1}' "
    # suspect that the dollar sign is bug
    #gsub("\\$", "\\\\$", data)
    #cmd = "printf \"%s\" \"" data "\" | sha256sum | awk '{print $1}'"
    # heredoc
    #cmd = "sha256sum <<< \"" data "\""# | awk '{print $1}'"

    # trying single-quote --- It Works !
    cmd = "printf \"%s\" '" data "' | sha256sum | awk '{print $1}'"

    cmd | getline hash
    close(cmd)

    return hash
}

function print_record(idx, record) {
    print idx
    for (i = 1; i <= NF; i++) {
        print record[i]
    }
}

BEGIN {
    FS = "|"
}
{
    lines[NR] = $0
    split($0, line, "|")

    old_hash = line[4]
    new_hash = get_sha256sum(line)

    print_record(NR,line)
    if (!found && new_hash != old_hash) {
        print "record no." NR " is bad"
        print "(old) " old_hash
        print "(now) " new_hash
        found = 1
    }

    if (found) {
        mining = -1
        while (1) {
            mining++
            line[2] = mining
            new_hash = get_sha256sum(line)
            if ( mining % 100 == 0 ) print "mining/",mining,"gen/",new_hash
            if (substr(new_hash, 1, 6) == "000000") {
                line[4] = new_hash
                if (NR < length(lines)) {
                    split(lines[NR + 1], next_record, "|")
                    next_record[3] = new_hash
                    lines[NR + 1] = next_record[1] FS next_record[2] FS next_record[3] FS next_record[4]
                }
                break
            }
        }
        print "(new) " line[4]
    }
    print ""
}

