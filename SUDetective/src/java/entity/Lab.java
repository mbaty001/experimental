/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package entity;

import java.io.Serializable;
import java.util.List;
import javax.persistence.*;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlTransient;

/**
 *
 * @author mbaty001
 */
@Entity
@Table(name = "LAB")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "Lab.findAll", query = "SELECT l FROM Lab l"),
    @NamedQuery(name = "Lab.findByIdLAB", query = "SELECT l FROM Lab l WHERE l.idLAB = :idLAB"),
    @NamedQuery(name = "Lab.findByName", query = "SELECT l FROM Lab l WHERE l.name = :name"),
    @NamedQuery(name = "Lab.findByNoOfLangs", query = "SELECT l FROM Lab l WHERE l.noOfLangs = :noOfLangs"),
    @NamedQuery(name = "Lab.findByHap", query = "SELECT l FROM Lab l WHERE l.hap = :hap"),
    @NamedQuery(name = "Lab.findByRms", query = "SELECT l FROM Lab l WHERE l.rms = :rms"),
    @NamedQuery(name = "Lab.findByDualIp", query = "SELECT l FROM Lab l WHERE l.dualIp = :dualIp")})
public class Lab implements Serializable, Comparable<Lab> {
    @Basic(optional = false)
    @NotNull
    @Column(name = "HAP")
    private String hap;
    @Basic(optional = false)
    @NotNull
    @Column(name = "RMS")
    private String rms;
    @Basic(optional = false)
    @NotNull
    @Column(name = "DUAL_IP")
    private String dualIp;
    private static final long serialVersionUID = 1L;
    @Id
    @Basic(optional = false)
    @NotNull
    @Column(name = "idLAB")
    private Integer idLAB;
    @Size(max = 2000000000)
    @Column(name = "NAME")
    private String name;
    @Basic(optional = false)
    @NotNull
    @Column(name = "NO_OF_LANGS")
    private int noOfLangs;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "lABidLAB")
    private List<Su> suList;
    @JoinColumn(name = "ACS_TYPE_idHW_TYPE", referencedColumnName = "idHW_TYPE")
    @ManyToOne(optional = false)
    private HwType aCSTYPEidHWTYPE;
    @JoinColumn(name = "IP_TYPE_idIP_TYPE", referencedColumnName = "idIP_TYPE")
    @ManyToOne(optional = false)
    private IpType iPTYPEidIPTYPE;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "lABidLAB")
    private List<Ts> tsList;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "lABidLAB")
    private List<Ms> msList;

    public int compareTo(Lab l){
        return name.compareTo(l.name);
    }
    
    public Lab() {
    }

    public Lab(Integer idLAB) {
        this.idLAB = idLAB;
    }

    public Lab(Integer idLAB, int noOfLangs, String hap, String rms, String dualIp) {
        this.idLAB = idLAB;
        this.noOfLangs = noOfLangs;
        this.hap = hap;
        this.rms = rms;
        this.dualIp = dualIp;
    }

    public Integer getIdLAB() {
        return idLAB;
    }

    public void setIdLAB(Integer idLAB) {
        this.idLAB = idLAB;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getNoOfLangs() {
        return noOfLangs;
    }

    public void setNoOfLangs(int noOfLangs) {
        this.noOfLangs = noOfLangs;
    }

    public String getDualIp() {
        return dualIp;
    }

    public void setDualIp(String dualIp) {
        this.dualIp = dualIp;
    }

    @XmlTransient
    public List<Su> getSuList() {
        return suList;
    }

    public void setSuList(List<Su> suList) {
        this.suList = suList;
    }

    public HwType getACSTYPEidHWTYPE() {
        return aCSTYPEidHWTYPE;
    }

    public void setACSTYPEidHWTYPE(HwType aCSTYPEidHWTYPE) {
        this.aCSTYPEidHWTYPE = aCSTYPEidHWTYPE;
    }

    public IpType getIPTYPEidIPTYPE() {
        return iPTYPEidIPTYPE;
    }

    public void setIPTYPEidIPTYPE(IpType iPTYPEidIPTYPE) {
        this.iPTYPEidIPTYPE = iPTYPEidIPTYPE;
    }

    @XmlTransient
    public List<Ts> getTsList() {
        return tsList;
    }

    public void setTsList(List<Ts> tsList) {
        this.tsList = tsList;
    }

    @XmlTransient
    public List<Ms> getMsList() {
        return msList;
    }

    public void setMsList(List<Ms> msList) {
        this.msList = msList;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (idLAB != null ? idLAB.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof Lab)) {
            return false;
        }
        Lab other = (Lab) object;
        if ((this.idLAB == null && other.idLAB != null) || (this.idLAB != null && !this.idLAB.equals(other.idLAB))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "entity.Lab[ idLAB=" + idLAB + " ]";
    }

    public String getHap() {
        return hap;
    }

    public void setHap(String hap) {
        this.hap = hap;
    }

    public String getRms() {
        return rms;
    }

    public void setRms(String rms) {
        this.rms = rms;
    }

}
