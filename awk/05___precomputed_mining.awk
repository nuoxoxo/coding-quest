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
    I_KNOW_THEM[1] = 4675746
    I_KNOW_THEM[2] = 10479258
    I_KNOW_THEM[3] = 1280359
    I_KNOW_THEM[4] = 18147393
    I_KNOW_THEM[5] = 35728140
    I_KNOW_THEM[6] = 821649
    I_KNOW_THEM[7] = 13953955
    I_KNOW_THEM[8] = 8447017
    I_KNOW_THEM[9] = 7103037
    I_KNOW_THEM[10] = 7034044
    I_KNOW_THEM[11] = 20596537
    I_KNOW_THEM[12] = 23807772
    I_KNOW_THEM[13] = 17511092
}
{
    lines[NR] = $0
    split($0, line, "|")
    if ( found )
        line [3] = res
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
        idx++
        mining = I_KNOW_THEM [idx]
        line[2] = mining
        new_hash = get_sha256sum(line)
        #if ( mining % 100 == 0 ) print "mining/",mining,"gen/",new_hash
        assert (substr(new_hash, 1, 6) == "000000")
        print "mining/",mining
        print "result/",new_hash
        res = new_hash
    }
    print ""
}
END {
    print "res/",res
}
