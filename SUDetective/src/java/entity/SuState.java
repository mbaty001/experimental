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
@Table(name = "SU_STATE")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "SuState.findAll", query = "SELECT s FROM SuState s"),
    @NamedQuery(name = "SuState.findByIdSUSTATE", query = "SELECT s FROM SuState s WHERE s.idSUSTATE = :idSUSTATE"),
    @NamedQuery(name = "SuState.findByName", query = "SELECT s FROM SuState s WHERE s.name = :name")})
public class SuState implements Serializable, Comparable<SuState> {
    private static final long serialVersionUID = 1L;
    @Id
    @Basic(optional = false)
    @NotNull
    @Column(name = "idSU_STATE")
    private Integer idSUSTATE;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 2000000000)
    @Column(name = "NAME")
    private String name;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "sUSTATEidSUSTATE")
    private List<Su> suList;

    public int compareTo(SuState ss){
        return name.compareTo(ss.name);
    }
    
    public SuState() {
    }

    public SuState(Integer idSUSTATE) {
        this.idSUSTATE = idSUSTATE;
    }

    public SuState(Integer idSUSTATE, String name) {
        this.idSUSTATE = idSUSTATE;
        this.name = name;
    }

    public Integer getIdSUSTATE() {
        return idSUSTATE;
    }

    public void setIdSUSTATE(Integer idSUSTATE) {
        this.idSUSTATE = idSUSTATE;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @XmlTransient
    public List<Su> getSuList() {
        return suList;
    }

    public void setSuList(List<Su> suList) {
        this.suList = suList;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (idSUSTATE != null ? idSUSTATE.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof SuState)) {
            return false;
        }
        SuState other = (SuState) object;
        if ((this.idSUSTATE == null && other.idSUSTATE != null) || (this.idSUSTATE != null && !this.idSUSTATE.equals(other.idSUSTATE))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "entity.SuState[ idSUSTATE=" + idSUSTATE + " ]";
    }
    
}
